using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class TakeDamage : MonoBehaviour
{
    public GameObject Bomb;
    public GameObject Bombo;
    public GameObject WhitebackGrund;
    public GameObject player;
    public GameObject player2;
    public GameObject hole;

    public Animator Healing;

    [Header("Heart UI")]
    public Image[] heartImages;

    [Header("Heart Sprites")]
    public Sprite heart3;
    public Sprite heart2;
    public Sprite heart1;
    public Sprite heart0;

    [Header("Health")]
    public int maxHealth = 9;

    public int damageAmount = 1;
    public int damageAmountminiGame = 1;

    private int health;

    [Header("Invincible")]
    public float invincibleTime = 1f;

    private bool isInvincible = false;

    void Start()
    {
        health = maxHealth;

        UpdateHeartUI();

        Bomb.SetActive(false);
        Bombo.SetActive(false);
        WhitebackGrund.SetActive(false);
        player.SetActive(false);
        player2.SetActive(false);
        hole.SetActive(false);
    }

    public void takeDamage()
    {
        if (isInvincible)
            return;

        isInvincible = true;

        health -= damageAmount;

        // กันค่าติดลบ
        health = Mathf.Max(health, 0);

        UpdateHeartUI();

        if (health <= 0)
        {
            Debug.Log("Game Over");
            StartCoroutine(Bomboo());

            FindFirstObjectByType<GameManager>().GameOver();
            return;
        }

        StartCoroutine(InvincibleCoroutine());
    }

    public void takeDamageMinigame()
    {
        if (isInvincible)
            return;

        isInvincible = true;

        health -= damageAmountminiGame;

        // กันค่าติดลบ
        health = Mathf.Max(health, 0);

        UpdateHeartUI();

        if (health <= 0)
        {
            Debug.Log("Game Over");
            StartCoroutine(Bomboo());

            FindFirstObjectByType<GameManager>().GameOver();
            return;
        }

        StartCoroutine(InvincibleCoroutine());
    }

    public void Heal(int healAmount)
    {
        Healing.SetTrigger("Heal");

        health += healAmount;

        // ห้ามเลือดต่ำกว่า 0 หรือสูงกว่า maxHealth
        health = Mathf.Clamp(health, 0, maxHealth);

        UpdateHeartUI();

        Debug.Log($"Heal +{healAmount} | HP: {health}/{maxHealth}");

    }

    private void UpdateHeartUI()
    {
        for (int i = 0; i < heartImages.Length; i++)
        {
            // หัวใจดวงนี้รับผิดชอบ HP ช่วงไหน
            int heartHealth = Mathf.Clamp(
                health - (i * 3),
                0,
                3
            );

            switch (heartHealth)
            {
                case 3:
                    heartImages[i].sprite = heart3;
                    break;

                case 2:
                    heartImages[i].sprite = heart2;
                    break;

                case 1:
                    heartImages[i].sprite = heart1;
                    break;

                case 0:
                    heartImages[i].sprite = heart0;
                    break;
            }
        }
    }

    IEnumerator InvincibleCoroutine()
    {
        Renderer[] renderers =
            GetComponentsInChildren<Renderer>();

        float timer = 0f;

        while (timer < invincibleTime)
        {
            foreach (Renderer r in renderers)
            {
                r.enabled = !r.enabled;
            }

            yield return new WaitForSeconds(0.1f);

            timer += 0.1f;
        }

        foreach (Renderer r in renderers)
        {
            r.enabled = true;
        }

        isInvincible = false;
    }

    IEnumerator White()
    {
        Renderer[] renderers =
        GetComponentsInChildren<Renderer>();

        // ซ่อนตัวละคร
        foreach (Renderer r in renderers)
        {
            r.enabled = false;
        }

        // รอตามเวลาที่กำหนด
        yield return new WaitForSecondsRealtime(invincibleTime);

        // แสดงตัวละครกลับม
    }

    IEnumerator Bomboo()
    {
        yield return new WaitForSecondsRealtime(0.1f);
        Bombo.SetActive(true);
        Renderer[] renderers =
        GetComponentsInChildren<Renderer>();

        // ซ่อนตัวละคร
        foreach (Renderer r in renderers)
        {
            r.enabled = false;
        }
        yield return new WaitForSecondsRealtime(0.2f);
        WhitebackGrund.SetActive(true);
        player.SetActive(true);

        yield return new WaitForSecondsRealtime(1.5f);
        player.SetActive(false);
        hole.SetActive(true);
        player2.SetActive(true);
        Bomb.SetActive(true);
    }


}