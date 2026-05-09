





import java.util.List;
import java.util.ArrayList;

public class stateMachineDsl_DoubleExp extends Expression {

    private String negative;
    private int decimal;
    private int number;



    public stateMachineDsl_DoubleExp(
        String negative,        int decimal,        int number    ) {
        super(
        );
        this.negative = negative;
        this.decimal = decimal;
        this.number = number;
    }


    public String getNegative() {
        return negative;
    }

    public void setNegative(String negative) {
        this.negative = negative;
    }
    public int getDecimal() {
        return decimal;
    }

    public void setDecimal(int decimal) {
        this.decimal = decimal;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }


}