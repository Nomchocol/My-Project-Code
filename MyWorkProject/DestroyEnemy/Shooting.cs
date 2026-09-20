using UnityEngine;

public class Shooting : MonoBehaviour
{
    public static Shooting instance;

    public Texture2D cursorTexture; // ใส่รูปเมาส์ใน Inspector
    public Vector2 hotSpot = Vector2.zero; // จุดกด (0,0 = มุมซ้ายบน)
    public CursorMode cursorMode = CursorMode.Auto;
    public Camera cam;
    public Animator gunAnimator;
    public Animator gunAnimator2;
    private bool swapgun = false;

    [Header("Gun1")]
    public GameObject muzzleFlashPrefab;
    [SerializeField] private Transform barrelLocation;

    [Header("Gun2")]
    public GameObject muzzleFlashPrefab2;
    [SerializeField] private Transform barrelLocation2;

    void Awake()
    {
        instance = this;
    }

    void Start()
    {
        Cursor.SetCursor(cursorTexture, hotSpot, cursorMode);

        if (barrelLocation2 == null)
            barrelLocation2 = transform;

        if (barrelLocation == null)
            barrelLocation = transform;
    }

    void Update()
    {
        if (Input.GetMouseButtonDown(0) && swapgun)
        {
            Ray ray = cam.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;
            Shoot();
            gun2();

            if (Physics.Raycast(ray, out hit))
            {
                if (hit.collider.CompareTag("Target"))
                {
                    EnemyHealth enemy = hit.collider.GetComponent<EnemyHealth>();
                    if (enemy != null)
                    {
                        enemy.TakeDamage(50);
                    }
                }
            }
        }

        else if (Input.GetMouseButtonDown(0) && !swapgun)
        {
            Ray ray = cam.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;
            Shoot2();
            gun1();

            if (Physics.Raycast(ray, out hit))
            {
                if (hit.collider.CompareTag("Target"))
                {
                    EnemyHealth enemy = hit.collider.GetComponent<EnemyHealth>();
                    if (enemy != null)
                    {
                        enemy.TakeDamage(50);
                    }
                }
            }
        }
    }

    public void Shoot()
    {
        if (muzzleFlashPrefab)
        {
            //Create the muzzle flash
            GameObject tempFlash;
            tempFlash = Instantiate(muzzleFlashPrefab, barrelLocation.position, barrelLocation.rotation);

            //Destroy the muzzle flash effect
            Destroy(tempFlash, 0.5f);
        }
    }


    public void Shoot2()
    {
        if (muzzleFlashPrefab2)
        {
            //Create the muzzle flash
            GameObject tempFlash;
            tempFlash = Instantiate(muzzleFlashPrefab2, barrelLocation2.position, barrelLocation2.rotation);

            //Destroy the muzzle flash effect
            Destroy(tempFlash, 0.5f);
        }
    }

    void gun1()
    {
        gunAnimator2.SetTrigger("Fire");
        swapgun = true;
    }

    void gun2()
    {
        gunAnimator.SetTrigger("Fire");
        swapgun = false;
    }
}
