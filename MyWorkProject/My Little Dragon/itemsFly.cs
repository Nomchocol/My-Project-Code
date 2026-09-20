using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class ItemsFly : MonoBehaviour
{
    public float respawnTime = 5f; 

    private Vector3 spawnPosition;
    private SpriteRenderer spriteRenderer; 
    private BoxCollider2D boxCollider;
    [SerializeField] private Image Flybartotal; 
    private bool itemFly = false; 
    private float fillSpeed = 0.5f;
    public float doubleTapTime = 0.5f;
    private float lastTapTime = 0;

    private void Start()
    {
        spawnPosition = transform.position;
        spriteRenderer = GetComponent<SpriteRenderer>(); 
        boxCollider = GetComponent<BoxCollider2D>();
        Flybartotal.fillAmount = 0;
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Player"))
        {
            Flybartotal.fillAmount = 1;
            PlayerFly player = other.GetComponent<PlayerFly>();
            if (player != null)
            {
                player.EnableFly();
                HideItem();
                StartCoroutine(RespawnItem());
            }
        }
    }

    public void HideItem()
    {
        if (spriteRenderer != null)
        {
            spriteRenderer.enabled = false; 
        }

        if (boxCollider !=  null)
        {
            boxCollider.enabled = false;
        }
    }

    public void ShowItem()
    {
        if (spriteRenderer != null)
        {
            spriteRenderer.enabled = true; 
        }

        if (boxCollider != null)
        {
            boxCollider.enabled = true;
        }
    }

    private IEnumerator RespawnItem()
    {
        yield return new WaitForSeconds(respawnTime);

        ShowItem();
        transform.position = spawnPosition; 
    }

    private void Update()
    {
        if (itemFly)
        {
            Flybartotal.fillAmount += fillSpeed * Time.deltaTime;

            if (Flybartotal.fillAmount >= 1)
            {
                Flybartotal.fillAmount = 1;
            }
        }

        if (Input.GetKeyDown(KeyCode.W))
        {
            if (Time.time - lastTapTime < doubleTapTime)
            {
                if (Input.GetKeyDown(KeyCode.W))
                {
                    Flybartotal.fillAmount = 0;
                }

            }
            lastTapTime = Time.time;

        }


    }
}
