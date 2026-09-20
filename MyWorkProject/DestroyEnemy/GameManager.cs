using UnityEngine;
using TMPro;   // ✅ ต้องใช้ namespace นี้
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    public static GameManager instance;

    public TMP_Text scoreText;     // ใช้ TextMeshPro
    public TMP_Text gameOverText;  // ข้อความ Game Over
    public GameObject buttonRestart;
    public GameObject lose1;
    public GameObject lose2;


    public int score = 0;
    private bool isGameOver = false;
    private AudioSource audioSource;  // ช่องเสียง
    private bool Sourcetrue = true;
    private bool Sourcetrue2 = true;
    public AudioClip clip;
    public AudioClip clip2;

    void Awake()
    {
        instance = this;
    }

    void Start()
    {
        if (audioSource == null)
        {
            audioSource = GetComponent<AudioSource>();
        }
        lose1.SetActive(false);
        lose2.SetActive(false);
        scoreText.text = "Total kills: " + score;
        gameOverText.gameObject.SetActive(false); // ซ่อน Game Over ตอนเริ่มเกม
        buttonRestart.gameObject.SetActive(false);
    }

    public void PlayOnce()
    {
        if (clip != null)
        {
            audioSource.PlayOneShot(clip); // เล่นครั้งเดียว
        }
    }

    public void PlayOnce2()
    {
        if (clip2 != null)
        {
            audioSource.PlayOneShot(clip2); // เล่นครั้งเดียว
        }
    }


    public void AddScore(int amount)
    {
        if (!isGameOver)
        {
            score += amount;
            scoreText.text = "Total kills: " + score;
        }
    }

    void glassbreak()
    {
        if (Sourcetrue)
        {
            GetComponent<GameManager>().PlayOnce();
            Sourcetrue = false;
        }
    }

    void glassbreak2()
    {
        if (Sourcetrue2)
        {
            GetComponent<GameManager>().PlayOnce2();
            Sourcetrue2 = false;
        }
    }


    public void GameOver()
    {
        glassbreak();
        lose1.SetActive(true);
        Invoke(nameof(GameOvernext), 0.3f);
    }

    public void GameOvernext()
    {
        glassbreak2();
        lose2.SetActive(true);
        Invoke(nameof(GameOvernext2), 0.5f);
    }

    public void GameOvernext2()
    {
        isGameOver = true;
        gameOverText.gameObject.SetActive(true);
        gameOverText.text = "You Died\nTotal kills: " + score;
        buttonRestart.gameObject.SetActive(true);
        Time.timeScale = 0;
    }



    public void RestartGame()
    {
        Time.timeScale = 1; // รีเซ็ตเวลาในเกม
        SceneManager.LoadScene(SceneManager.GetActiveScene().name); // โหลดฉากปัจจุบันใหม่
    }

    public void nextscene2()
    {
        SceneManager.LoadScene("SceneCar");
    }
}
