





import java.util.List;
import java.util.ArrayList;

public class ptnet_Deterministic extends Distribution {

    private float Value;



    public ptnet_Deterministic(
        float Value    ) {
        super(
        );
        this.Value = Value;
    }


    public float getValue() {
        return Value;
    }

    public void setValue(float Value) {
        this.Value = Value;
    }


}