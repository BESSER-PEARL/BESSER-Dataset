





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_QUDV_Prefix  {

    private String name;
    private String symbol;





    private Rational rational;


    public SysML_ValueTypes_QUDV_QUDV_Prefix(
        String name,        String symbol    ) {
        this.name = name;
        this.symbol = symbol;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public Rational getRational() {
        return rational;
    }

    public void setRational(Rational rational) {
        this.rational = rational;
    }

}