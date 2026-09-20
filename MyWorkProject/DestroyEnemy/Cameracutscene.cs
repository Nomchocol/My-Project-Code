using UnityEngine;
using TMPro;
using TMPro.Examples;

public class Cameracutscene : MonoBehaviour
{
    public static Cameracutscene instance;

    private Quaternion targetRotation; // การหมุนเป้าหมาย (ตำแหน่งเดิม)
    private Quaternion startRotation;
    private Quaternion targetgun;
    private Quaternion targetgun2;
    public TMP_Text subText;
    public GameObject Gun1;
    public GameObject Gun2;
    public GameObject notshoot1;
    private AudioSource audioSource;  // ช่องเสียง
    public AudioClip clip;           // ไฟล์เสียงที่จะเล่น
    public AudioClip clip2;

    private bool startgame = true;
    private bool isRotatinggun = false;
    private bool isRotating = false;
    private bool fighting = false;
    private bool walk = false;
    private bool soundgun = false;
    public bool stop = false;
    public bool stop2 = false;
    private bool newstop = false;
    private bool newstop2 = false;
    private bool newstop3 = false;
    public bool spawnnew = false;
    public bool startnextscene = false;
    private bool reloadgun = false;

    void Awake()
    {
        instance = this;
    }

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        if (audioSource == null)
        {
            audioSource = GetComponent<AudioSource>();
        }
        notshoot1.SetActive(true);

        targetgun = Quaternion.Euler(-182.126f, 0, -180);
        targetgun2 = Quaternion.Euler(-182.126f, 0, -180);
        targetRotation = Quaternion.Euler(0, 120, 0);
        startRotation = Quaternion.Euler(transform.eulerAngles.x, transform.eulerAngles.y, transform.eulerAngles.z);

        transform.rotation = startRotation;

        subText.gameObject.SetActive(false);
    }

    // Update is called once per frame
    void Update()
    {

        if (Input.GetMouseButtonDown(0) && soundgun)
        {
            GetComponent<Cameracutscene>().PlayOnce();
        }

        if (transform.position.x == 8.746f && startgame)
        {
            transform.position = Vector3.MoveTowards(transform.position, new Vector3(transform.position.x, transform.position.y, 4.27f), Time.deltaTime * 2.5f);
            if (transform.position.z == 4.27f)
            {
                startgame = false;
            }
        }
        
        if (isRotating)
        {
            // ค่อย ๆ หมุนกล้องจาก startRotation ไป targetRotation
            transform.rotation = Quaternion.Lerp(transform.rotation, targetRotation, Time.deltaTime * 7);

            if (Quaternion.Angle(transform.rotation, targetRotation) < 0.1f)
            {
                transform.rotation = targetRotation; // ตั้งค่าให้ตรงเป้าหมาย
                isRotating = false; // หยุดการหมุน
            }
        }

        if (transform.position.z == 4.27f && Quaternion.Angle(transform.rotation, Quaternion.Euler(0, 180, 0)) < 0.1f)
        {

            Invoke(nameof(rotateCamera), 0.5f);
        }

        if (transform.position.y == 2.244f && Quaternion.Angle(transform.rotation, Quaternion.Euler(0, 120, 0)) < 0.1f)
        {
            transform.position = Vector3.MoveTowards(transform.position, new Vector3(8.747f, transform.position.y, 5.41f), Time.deltaTime * 7f);
        }

        if (transform.position.z == 5.41f && transform.rotation == Quaternion.Euler(0, 120, 0))
        {
            subText.gameObject.SetActive(true);
            subText.text = "เชี่ยเอ้ย! ใครวะน่ะ ทำไมมาอยู่บ้านตรูฟะ";
            Invoke(nameof(textsub), 2.3f);
        }

        if (isRotatinggun)
        {
            Gun1.transform.rotation = Quaternion.Lerp(Gun1.transform.rotation, targetgun, Time.deltaTime * 2.5f);
            Gun2.transform.rotation = Quaternion.Lerp(Gun2.transform.rotation, targetgun2, Time.deltaTime * 2.5f);
            Invoke(nameof(fight), 2.5f);
        }

        if (transform.position.x == 8.747f && fighting)
        {
            notshoot1.SetActive(false);
            subText.text = "";
            transform.position = Vector3.MoveTowards(transform.position, new Vector3(8.747f, transform.position.y, 3.71f), Time.deltaTime * 5f);
            if (transform.position.z == 3.71f)
            {
                targetRotation = Quaternion.Euler(0, 90, 0);
                isRotating = true;
                stop2 = true;
                if (Quaternion.Angle(transform.rotation, Quaternion.Euler(0, 90, 0)) < 0.1f)
                {
                    fighting = false;
                }
            }
        }

        if (GameManager.instance.score == 2 && !stop)
        {
            Invoke(nameof(go), 0.5f);
            if (walk)
            {
                transform.position = Vector3.MoveTowards(transform.position, new Vector3(12.611f, transform.position.y, 3.71f), Time.deltaTime * 2.5f);
                if (transform.position.x == 12.611f)
                {
                    stop = true;
                    stop2 = false;
                }
            }
        }
        else if (GameManager.instance.score < 2 && stop2)
        {
            Invoke(nameof(GameOver0), 1.5f);
        }

        if (GameManager.instance.score == 3 && stop)
        {
            Invoke(nameof(go2), 0.5f);
            if (!walk)
            {
                transform.position = Vector3.MoveTowards(transform.position, new Vector3(14.195f, transform.position.y, 3.71f), Time.deltaTime * 2.5f);
                {
                    if (transform.position.x == 14.195f)
                    {
                        targetRotation = Quaternion.Euler(0, 3.878f, 0);
                        isRotating = true;
                        stop = false;
                        newstop = true;
                    }

                }
            }
        }
        else if (GameManager.instance.score < 3 && stop)
        {
            Invoke(nameof(GameOver1), 0.5f);
        }

        if (GameManager.instance.score == 6 && newstop)
        {
            Invoke(nameof(go), 0.5f);
            if (walk)
            {
                targetRotation = Quaternion.Euler(0, 110.324f, 0);
                isRotating = true;
            }
        }
        else if (GameManager.instance.score < 6 && newstop)
        {
            Invoke(nameof(GameOver2), 1.5f);
        }

        if (transform.position.y == 2.244f && Quaternion.Angle(transform.rotation, Quaternion.Euler(0, 110.324f, 0)) < 0.1f)
        {
            transform.position = Vector3.MoveTowards(transform.position, new Vector3(17.50000f, transform.position.y, 2.50000f), Time.deltaTime * 2.5f);
            if (transform.position.x == 17.50000f)
            {
                targetRotation = Quaternion.Euler(0, 0, 0);
                isRotating = true;
                newstop = false;
            }
        }

        if (GameManager.instance.score == 7)
        {
            Invoke(nameof(go2), 0.5f);
            if (!walk)
            {
                transform.position = Vector3.MoveTowards(transform.position, new Vector3(17.50000f, transform.position.y, 8.967f), Time.deltaTime * 2.5f);
                if (transform.position.z == 8.967f && !spawnnew)
                {
                    spawnnew = true;
                    newstop2 = true;
                }
            }
        }

        if (GameManager.instance.score >= 9 && newstop2)
        {
            Invoke(nameof(go), 0.5f);
            if (walk)
            {
                targetRotation = Quaternion.Euler(0, 325.653f, 0);
                isRotating = true;
                if (Quaternion.Angle(transform.rotation, Quaternion.Euler(0, 325.653f, 0)) < 0.1f)
                {
                    transform.position = Vector3.MoveTowards(transform.position, new Vector3(16.3409996f, transform.position.y, 10.6630001f), Time.deltaTime * 2.5f);
                }
            }

        }
        else if (GameManager.instance.score < 9 && newstop2)
        {
            Invoke(nameof(GameOver3), 1.2f);
        }

        if (transform.position.x == 16.3409996f)
        {
            targetRotation = Quaternion.Euler(0, 270, 0);
            isRotating = true;
            newstop2 = false;
        }

        if (Quaternion.Angle(transform.rotation, Quaternion.Euler(0, 270, 0)) < 0.1f)
        {
            transform.position = Vector3.MoveTowards(transform.position, new Vector3(6.5f, transform.position.y, 10.6630001f), Time.deltaTime * 2.5f);
            newstop3 = true;
        }

        if (GameManager.instance.score == 14 && newstop3)
        {
            if (transform.position.x == 6.5f)
            {
                targetRotation = Quaternion.Euler(0, 339.179f, 0);
                isRotating = true;
                startnextscene = true;
                if (Quaternion.Angle(transform.rotation, Quaternion.Euler(0, 339.179f, 0)) < 0.1f)
                {
                    subText.text = "เชี่ยเอ้ยยยยยยยย";
                    soundgun = false;
                }
            }
        }
        else if (GameManager.instance.score < 14 && newstop3)
        {
            Invoke(nameof(GameOver4), 2.5f);
        }
    }

    void reload()
    {
        if (!reloadgun )
        {
            GetComponent<Cameracutscene>().PlayOnce2();
            reloadgun = true;
        }
        
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


    void rotateCamera()
    {
        isRotating = true;
    }

    void textsub()
    {
        reload();
        subText.text = " ไม่ได้การอย่างงี้ต้องกำจัด";
        soundgun = true;
        targetRotation = Quaternion.Euler(0, 180, 0);
        isRotating = true;
        isRotatinggun = true;
        
    }

    void fight()
    {
        fighting = true;
        isRotatinggun = false;
    }


    void go()
    {
        walk = true;
    }

    void go2()
    {
        walk = false;
    }

    void GameOver(int Score)
    {
        if (GameManager.instance.score < Score)
        {
            GameManager.instance.GameOver();
        }
    }

    void GameOver0() => GameOver(2);
    void GameOver1() => GameOver(3);
    void GameOver2() => GameOver(6);
    void GameOver3() => GameOver(9);
    void GameOver4() => GameOver(14);
}
