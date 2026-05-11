





import java.util.List;
import java.util.ArrayList;

public class minilang_Constant extends Value {

    private float value;



    public minilang_Constant(
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