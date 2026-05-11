





import java.util.List;
import java.util.ArrayList;

public class cobol_literals_NationalHexLiteral extends DBCSLiteral {

    private float value;



    public cobol_literals_NationalHexLiteral(
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