





import java.util.List;
import java.util.ArrayList;

public class roverml_SingleQuantity extends Quantity {

    private float value;



    public roverml_SingleQuantity(
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