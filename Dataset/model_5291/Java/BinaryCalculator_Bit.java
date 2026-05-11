





import java.util.List;
import java.util.ArrayList;

public class BinaryCalculator_Bit extends BitSeq {

    private String value;





    private BinaryCalculator_L binarycalculator_l;


    public BinaryCalculator_Bit(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public BinaryCalculator_L getBinarycalculator_l() {
        return binarycalculator_l;
    }

    public void setBinarycalculator_l(BinaryCalculator_L binarycalculator_l) {
        this.binarycalculator_l = binarycalculator_l;
    }

}