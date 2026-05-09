





import java.util.List;
import java.util.ArrayList;

public class ptnet_GSPNImmediateTransition extends GSPNTransition {

    private float Weight;
    private int Priority;



    public ptnet_GSPNImmediateTransition(
        float Weight,        int Priority    ) {
        super(
        );
        this.Weight = Weight;
        this.Priority = Priority;
    }


    public float getWeight() {
        return Weight;
    }

    public void setWeight(float Weight) {
        this.Weight = Weight;
    }
    public int getPriority() {
        return Priority;
    }

    public void setPriority(int Priority) {
        this.Priority = Priority;
    }


}