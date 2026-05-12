





import java.util.List;
import java.util.ArrayList;

public class statechartexpressions_TimeConstant extends TimeExpression {

    private String unit;
    private int value;



    public statechartexpressions_TimeConstant(
        String unit,        int value    ) {
        super(
        );
        this.unit = unit;
        this.value = value;
    }


    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}