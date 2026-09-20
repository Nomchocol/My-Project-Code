using UnityEngine;

public class GroundTileTrigger : MonoBehaviour
{
    private GroundTile groundTile;

    private void Awake()
    {
        groundTile = GetComponentInParent<GroundTile>();

        if (groundTile == null)
        {
            Debug.LogError(
                "Trigger นี้ไม่มี GroundTile อยู่ที่ Parent",
                gameObject
            );
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        Debug.Log("Trigger ชนกับ: " + other.name);

        if (!other.CompareTag("Player"))
            return;

        Debug.Log("Player ผ่าน Trigger ของ: " + groundTile.name);

        groundTile.Recycle();
    }
}