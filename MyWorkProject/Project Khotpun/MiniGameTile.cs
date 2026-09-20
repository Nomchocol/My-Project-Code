using UnityEngine;

public class MiniGameTile : GroundTile
{
    private MinigameBrakeTrigger brakeTrigger;

    private void Awake()
    {
        brakeTrigger =
            GetComponentInChildren<MinigameBrakeTrigger>(true);

        if (brakeTrigger == null)
        {
            Debug.LogError(
                $"{name} ไม่พบ MinigameBrakeTrigger ใน Object ลูก",
                gameObject
            );
        }
    }

    public override void ResetTile()
    {
        base.ResetTile();

        if (brakeTrigger != null)
        {
            brakeTrigger.ResetTrigger();
        }
    }
}