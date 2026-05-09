





import java.util.List;
import java.util.ArrayList;

public class stateMachineDsl_NumberExp extends Expression {

    private String negative;
    private int value;



    public stateMachineDsl_NumberExp(
        String negative,        int value    ) {
        super(
        );
        this.negative = negative;
        this.value = value;
    }


    public String getNegative() {
        return negative;
    }

    public void setNegative(String negative) {
        this.negative = negative;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}