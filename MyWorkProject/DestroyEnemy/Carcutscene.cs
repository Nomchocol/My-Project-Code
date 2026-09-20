using UnityEngine;

public class Carcutscene : MonoBehaviour
{
    public static Carcutscene instance;

    public void Update()
    {
        if (CameraScene.instance.startCutscene == true)
        {
            transform.position = Vector3.MoveTowards(transform.position, new Vector3(transform.position.x, transform.position.y, -300), Time.deltaTime * 20);
        }
    }
}
