





import java.util.List;
import java.util.ArrayList;

public class ram_LiteralDouble extends LiteralSpecification {

    private float value;



    public ram_LiteralDouble(
        float value    ) {
        super(
        );
        this.value = value;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }


}