using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections;

public class GameManager : MonoBehaviour
{
    public LeaderBoard leaderboard;

    public ScoreManager scoreManager;

    public GameObject gameOverPanel;
    public GameObject UIgameRun;
    public GameObject UI_MENU;
    public PauseManager Pause;

    public GameObject transitionEnd;
    public GameObject transitionStart;

    public GameObject tblackStart;

    public TMPro.TMP_Text timerText;

    public TMPro.TMP_Text scoreGameOverText;
    public TMPro.TMP_Text timeGameOverText;

    private float gameTime = 0f;

    private int finalScore;
    private float finalTime;

    public static bool isRestarting = false;

    void Start()
    {
        gameOverPanel.SetActive(false);
        transitionEnd.SetActive(false);

        if (isRestarting)
        {
            tblackStart.SetActive(false);
            transitionStart.SetActive(true);
            UI_MENU.SetActive(false);
            UIgameRun.SetActive(true);
            Pause.enabled = true;

            Time.timeScale = 1f;

            isRestarting = false;
        }
        else
        {
            tblackStart.SetActive(true);
            transitionStart.SetActive(false);
            UI_MENU.SetActive(true);
            UIgameRun.SetActive(false);
            Pause.enabled = false;
        }
    }
    void Update()
    {
        if (UIgameRun.activeSelf)
        {
            gameTime += Time.deltaTime;
        }

        gameTime += Time.deltaTime;

        int minutes = Mathf.FloorToInt(gameTime / 60f);
        int seconds = Mathf.FloorToInt(gameTime % 60f);

        timerText.text = string.Format("{0:00}:{1:00}", minutes, seconds);
    }

    public void RestartGame()
    {
        isRestarting = true;

        StartCoroutine(TransitionToScene());
    }

    public void GameOver()
    {
        // บันทึกค่าตอนจบเกม
        finalScore = Mathf.FloorToInt(scoreManager.score);
        finalTime = gameTime;

        // แสดงข้อมูลใน Game Over
        scoreGameOverText.text = finalScore.ToString();

        int minutes = Mathf.FloorToInt(finalTime / 60f);
        int seconds = Mathf.FloorToInt(finalTime % 60f);

        timeGameOverText.text = string.Format("{0:00}:{1:00}", minutes, seconds);

        Pause.enabled = false;
        StartCoroutine(DelayedGameOver());
    }

    public void QuitGame()
    {
        Application.Quit();
    }

    IEnumerator DelayedGameOver()
    {
        yield return new WaitForSeconds(0.14f);
        Time.timeScale = 0.75f;
        yield return new WaitForSeconds(0.05f);
        Time.timeScale = 0.25f;
        yield return new WaitForSeconds(0.05f);
        Time.timeScale = 0f;
        yield return new WaitForSecondsRealtime(3f);
        yield return leaderboard.SubmitScoreRoutine(Mathf.FloorToInt(scoreManager.score));

        gameOverPanel.SetActive(true);
    }
    IEnumerator TransitionToScene()
    {
        transitionEnd.SetActive(true);
        yield return new WaitForSecondsRealtime(1f);
        Time.timeScale = 1f;
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }
}