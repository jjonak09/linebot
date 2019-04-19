package main

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"math/rand"
	"net/http"
	"os"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/line/line-bot-sdk-go/linebot"
)

type VtuberInfo struct {
	Id        int    `json:"id"`
	Name      string `json:"name"`
	Nickname  string `json:"nickname"`
	Belong    string `json:"belong"`
	Twiiter   string `json:"twiiter"`
	ChannelId string `json:"channel_id"`
}

func main() {
	port := os.Getenv("PORT")

	if port == "" {
		log.Fatal("$PORT must be set")
	}

	bot, err := linebot.New(
		os.Getenv("CHANNEL_SECRET"),
		os.Getenv("CHANNEL_TOKEN"),
	)
	if err != nil {
		log.Fatal(err)
	}

	router := gin.New()
	router.Use(gin.Logger())
	router.LoadHTMLGlob("templates/*.tmpl.html")
	router.Static("/static", "static")

	//router.GET(path,handler)
	router.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "index.tmpl.html", nil)
	})

	router.POST("/callback", func(c *gin.Context) {
		events, err := bot.ParseRequest(c.Request)
		if err != nil {
			if err == linebot.ErrInvalidSignature {
				log.Print(err)
			}
			return
		}
		for _, event := range events {
			if event.Type == linebot.EventTypeMessage {
				switch message := event.Message.(type) {
				case *linebot.TextMessage:
					resmassage := RecommandVtuber(message.Text)
					if _, err = bot.ReplyMessage(event.ReplyToken, linebot.NewTextMessage(resmassage)).Do(); err != nil {
						log.Print(err)
					}
				}
			}
		}
	})

	router.Run(":" + port)
}

func RecommandVtuber(reqmessage string) (message string) {

	url := GetApiUrl()
	res, err := http.Get(string(url))
	if err != nil {
		log.Fatal(err)
	}
	defer res.Body.Close()

	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		log.Fatal(err)
	}
	var vtuber []VtuberInfo

	if err := json.Unmarshal(body, &vtuber); err != nil {
		log.Fatal(err)
	}
	rand.Seed(time.Now().UnixNano())
	num := rand.Intn(len(vtuber))
	if reqmessage == "hello" {
		return "hello"
	} else {
		message = vtuber[num].Name + "はいいぞ!" + GetYoutubeUrl() + vtuber[num].ChannelId
	}
	return message
}

func GetApiUrl() string {
	return "https://youtuberapi.herokuapp.com/api/vtuber?format=json"
}

func GetYoutubeUrl() string {
	return "https://www.youtube.com/channel/"
}
