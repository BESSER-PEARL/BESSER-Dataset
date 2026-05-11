





import java.util.List;
import java.util.ArrayList;

public class cobol_literals_IntegerLiteral extends water_FileDescriptorWater, water_IOControlParagraphWater, water_ObjectComputerParagraphWater, literals_NumericLiteral {

    private float value;



    public cobol_literals_IntegerLiteral(
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