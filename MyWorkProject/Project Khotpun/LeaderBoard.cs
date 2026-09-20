using UnityEngine;
using System.Collections;
using LootLocker.Requests;
using TMPro;
using UnityEngine.UIElements;

public class LeaderBoard : MonoBehaviour
{
    string leaderboardID = "36152";
    public TextMeshProUGUI playerNames;
    public TextMeshProUGUI playerScores;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    public IEnumerator SubmitScoreRoutine(int scoreToUpload)
    {
        bool done = false;
        string playerID = PlayerPrefs.GetString("PlayerID");
        LootLockerSDKManager.SubmitScore(playerID, scoreToUpload, leaderboardID, (response) =>
        {
            if (response.success)
            {
                Debug.Log("Successfully uploaded score");
                done = true;
            }
            else
            {
                Debug.LogError("Failed to upload score");
                done = true;
            }
        });
        yield return new WaitWhile(()=>done == false);
    }

    public IEnumerator FetchTopHighscoresRoutine()
    {
        bool done = false;
        LootLockerSDKManager.GetScoreList(leaderboardID, 10, 0, (response) =>
        {
            if (response.success)
            {
                string tempPlayerNames = "Names\n";
                string tempPlayerScores = "Score\n";

                LootLockerLeaderboardMember[] members = response.items;

                for (int i = 0; i < members.Length; i++)
                {
                    tempPlayerNames += members[i].rank + ". ";
                    if (members[i].player.name != "")
                    {
                        tempPlayerNames += members[i].player.name;
                    }
                    else
                    {
                        tempPlayerNames += members[i].player.id;
                    }
                    tempPlayerScores += members[i].score + "\n";
                    tempPlayerNames += "\n";
                }
                done = true;
                playerNames.text = tempPlayerNames;
                playerScores.text = tempPlayerScores;
            }
            else
            {
                Debug.LogError("Failed to upload score");
                done = true;
            }
        });
        yield return new WaitWhile(() => done == false);
    }
}