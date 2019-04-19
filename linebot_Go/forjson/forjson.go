package forjson

// web APIからの情報を保持する構造体
type PersonInfo struct {
	ID        int    `json:"id"`
	Name      string `json:"name"`
	Nickname  string `json:"nickname"`
	Belong    string `json:"belong"`
	Twiiter   string `json:"twiiter"`
	ChannelID string `json:"channel_id"`
}

//dialogflowへのresponseを保持する構造体
type Response struct {
	FulfillmentMessages []Text2 `json:"fulfillmentMessages"`
}

type Text2 struct {
	TextMessage Text `json:"text"`
}
type Text struct {
	TextList []string `json:"text"`
}

//dialogflowからのrequestを保持する構造体
type DialogflowRequest struct {
	ResponseID  string `json:"responseId"`
	QueryResult struct {
		QueryText  string `json:"queryText"`
		Parameters struct {
			BelongingAgency string `json:"belonging_agency"`
			YoutuberVtuber  string `json:"youtuber_vtuber"`
			YoutuberTag     string `json:"youtuber_tag"`
			Any             string `json:"any"`
		} `json:"parameters"`
		AllRequiredParamsPresent bool `json:"allRequiredParamsPresent"`
		FulfillmentMessages      []struct {
			Text struct {
				Text []string `json:"text"`
			} `json:"text"`
		} `json:"fulfillmentMessages"`
		Intent struct {
			Name        string `json:"name"`
			DisplayName string `json:"displayName"`
		} `json:"intent"`
		IntentDetectionConfidence int `json:"intentDetectionConfidence"`
		DiagnosticInfo            struct {
			WebhookLatencyMs int `json:"webhook_latency_ms"`
		} `json:"diagnosticInfo"`
		LanguageCode string `json:"languageCode"`
	} `json:"queryResult"`
	WebhookStatus struct {
		Message string `json:"message"`
	} `json:"webhookStatus"`
}

//Youtube API からのresponseを格納する
type YoutubeAPI struct {
	Kind          string `json:"kind"`
	Etag          string `json:"etag"`
	NextPageToken string `json:"nextPageToken"`
	RegionCode    string `json:"regionCode"`
	PageInfo      struct {
		TotalResults   int `json:"totalResults"`
		ResultsPerPage int `json:"resultsPerPage"`
	} `json:"pageInfo"`
	Items []struct {
		Kind string `json:"kind"`
		Etag string `json:"etag"`
		ID   struct {
			Kind    string `json:"kind"`
			VideoID string `json:"videoId"`
		} `json:"id"`
	} `json:"items"`
}
