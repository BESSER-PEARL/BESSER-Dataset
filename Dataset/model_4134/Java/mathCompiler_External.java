





import java.util.List;
import java.util.ArrayList;

public class mathCompiler_External extends Expression {

    private int exponent;
    private int base;



    public mathCompiler_External(
        int exponent,        int base    ) {
        super(
        );
        this.exponent = exponent;
        this.base = base;
    }


    public int getExponent() {
        return exponent;
    }

    public void setExponent(int exponent) {
        this.exponent = exponent;
    }
    public int getBase() {
        return base;
    }

    public void setBase(int base) {
        this.base = base;
    }


}