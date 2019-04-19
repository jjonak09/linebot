package main

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"math/rand"
	"net/http"
	"os"
	"time"

	"github.com/heroku/go-getting-started/forjson"

	"github.com/gin-gonic/gin"
)

func main() {
	port := os.Getenv("PORT")

	if port == "" {
		log.Fatal("$PORT must be set")
	}

	youtubeAPIKey := os.Getenv("YOUTUBEAPIKEY")

	router := gin.New()
	router.Use(gin.Logger())

	router.POST("/callback", func(c *gin.Context) {
		var req forjson.DialogflowRequest
		c.Bind(&req)

		persontype := req.QueryResult.Parameters.YoutuberVtuber
		belong := req.QueryResult.Parameters.BelongingAgency
		tag := req.QueryResult.Parameters.YoutuberTag
		name := req.QueryResult.Parameters.Any

		var res []string
		var resmessage forjson.Response
		if req.QueryResult.Intent.DisplayName == "recommand_youtuber" {
			res = Recommend(persontype, belong, tag)
		}
		if req.QueryResult.Intent.DisplayName == "take_new_video" {
			res = TakeNewVideo(name, youtubeAPIKey)
		}
		resmessage = MakeResponseMessage(res)

		c.JSON(200, resmessage)
	})

	router.Run(":" + port)
}

func Recommend(persontype string, belong string, tag string) []string {

	url := GetAPIURL() + persontype + "/?format=json"
	if tag != "" {
		url += "&tag=" + tag
	}
	if belong != "" {
		url += "&belong=" + belong
	}

	res, err := http.Get(string(url))
	if err != nil {
		log.Fatal(err)
	}
	defer res.Body.Close()

	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		log.Fatal(err)
	}
	var person []forjson.PersonInfo

	if err := json.Unmarshal(body, &person); err != nil {
		log.Fatal(err)
	}
	rand.Seed(time.Now().UnixNano())
	num := rand.Intn(len(person))
	message := []string{person[num].Name + "はいいぞ!", "https://www.youtube.com/channel/" + person[num].ChannelID}
	return message
}

func TakeNewVideo(name string, apikey string) []string {
	url := GetAPIURL() + "vtuber" + "/?format=json" + "&name=" + name
	res, err := http.Get(string(url))
	if err != nil {
		log.Fatal(err)
	}
	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		log.Fatal(err)
	}
	res.Body.Close()

	if string(body) == "[]" {
		url := GetAPIURL() + "youtuber" + "/?format=json" + "&name=" + name
		res, err := http.Get(string(url))
		if err != nil {
			log.Fatal(err)
		}
		body, err = ioutil.ReadAll(res.Body)
		if err != nil {
			log.Fatal(err)
		}
		res.Body.Close()
	}

	var p []forjson.PersonInfo
	if err := json.Unmarshal(body, &p); err != nil {
		log.Fatal(err)
	}
	url = GetYoutubeAPI() + p[0].ChannelID + "&order=date&key=" + apikey
	res, err = http.Get(string(url))
	if err != nil {
		log.Fatal(err)
	}
	defer res.Body.Close()
	b, err := ioutil.ReadAll(res.Body)
	if err != nil {
		log.Fatal(err)
	}
	var apiresponse forjson.YoutubeAPI
	if err := json.Unmarshal(b, &apiresponse); err != nil {
		log.Fatal(err)
	}
	newvideo := "https://www.youtube.com/watch?v=" + apiresponse.Items[0].ID.VideoID

	message := []string{"最新動画だぞ!", newvideo}
	return message
}

func GetAPIURL() string {
	return "https://youtuberapi.herokuapp.com/api/"
}

func GetYoutubeAPI() string {
	return "https://www.googleapis.com/youtube/v3/search?part=id&channelId="
}

func MakeResponseMessage(message []string) forjson.Response {
	resmessage1 := []string{message[0]}
	resmessage2 := []string{message[1]}
	textlist1 := forjson.Text{TextList: resmessage1}
	textlist2 := forjson.Text{TextList: resmessage2}
	text1 := forjson.Text2{textlist1}
	text2 := forjson.Text2{textlist2}
	res := []forjson.Text2{text1, text2}
	return forjson.Response{res}
}
