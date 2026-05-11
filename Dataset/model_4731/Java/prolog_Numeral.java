





import java.util.List;
import java.util.ArrayList;

public class prolog_Numeral extends Term {

    private float value;



    public prolog_Numeral(
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