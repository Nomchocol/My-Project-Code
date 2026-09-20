using UnityEngine;

public class MainCamera : MonoBehaviour
{
    public Transform player;

    public Vector3 offset = new Vector3(0f, 5f, -8f);
    public float smoothSpeed = 5f;

    void LateUpdate()
    {
        Vector3 targetPosition = player.position + offset;

        transform.position = Vector3.Lerp(
            transform.position,
            targetPosition,
            smoothSpeed * Time.deltaTime
        );
    }
}