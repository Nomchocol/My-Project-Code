using UnityEngine;
using TMPro;

public class ScoreManager : MonoBehaviour
{
    public Transform player;
    public TextMeshProUGUI scoreText;

    public TextMeshProUGUI miniGameText;

    public PlayerController warpminiGame1;

    public PauseManager Pause;

    public int miniGameScore;

    // คะแนนที่ได้เพิ่ม เช่น จาก Minigame
    public int bonusScore = 0;

    public float score;
    float lastScore;
    float idleTime;

    float startDelay = 1f;
    float timer = 0f;

    public float maxIdleTime = 1f;

    void Update()
    {
        timer += Time.deltaTime;

        if (timer < startDelay)
            return;

        // คะแนนจากระยะทาง + คะแนนโบนัส
        score = Mathf.Max(0, Mathf.Floor(player.position.x)) + bonusScore;

        scoreText.text = score.ToString();

        // เช็คว่า score เพิ่มไหม
        if (score > lastScore)
        {
            idleTime = 0f;
        }
        else
        {
            idleTime += Time.deltaTime;
        }

        // ถ้าอยู่นิ่งเกินกำหนด → Game Over
        if (warpminiGame1.miniGame1 == false)
        {
            if (idleTime >= maxIdleTime)
            {
                Debug.Log("Game Over");

                FindFirstObjectByType<GameManager>().GameOver();
            }
        }

        lastScore = score;

        miniGameText.text = "MiniGame: " + miniGameScore.ToString();
    }

    // เพิ่ม Score ปกติ
    public void AddScore(int amount)
    {
        bonusScore += amount;
    }

    // เพิ่มคะแนน Minigame
    public void AddMiniGameScore(int amount)
    {
        miniGameScore += amount;
    }

    public void RemoveMiniGameScore(int amount)
    {
        miniGameScore = Mathf.Max(0, miniGameScore - amount);
    }
}