using System.Collections;
using UnityEngine;
using LootLocker.Requests;
using TMPro;

public class PlayerManager : MonoBehaviour
{
    public LeaderBoard leaderboard;

    public TMP_InputField playerNameInputfield;

    void Start()
    {
        StartCoroutine(SetupRoutine());
    }

    public void SetPlayerName()
    {
        LootLockerSDKManager.SetPlayerName(playerNameInputfield.text, (response) =>
        {
            if (response.success)
            {
                Debug.Log("Sussesfully set player name");
            }
            else
            {
                Debug.LogError("Could not set player name");
            }
        });
    }

    IEnumerator SetupRoutine()
    {
        yield return LoginRoutine();
        yield return leaderboard.FetchTopHighscoresRoutine();
    }

    IEnumerator LoginRoutine()
    {
        bool done = false;
        LootLockerSDKManager.StartGuestSession((response) =>
        {
            if (response.success)
            {
                Debug.Log("Player was Logged in");
                PlayerPrefs.SetString("PlayerId", response.player_id.ToString());
                done = true;
            }
            else
            {
                Debug.Log("Could not Start session");
                done = true;
            }
        });
        yield return new WaitWhile(() => done == false); 
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
