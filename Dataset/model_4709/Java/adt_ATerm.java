





import java.util.List;
import java.util.ArrayList;

public class adt_ATerm  {

    private String symbol;





    private adt_Equation adt_equation;




    private adt_ASort adt_asort;




    private adt_ADT adt_adt;




    private adt_Equation adt_equation;


    public adt_ATerm(
        String symbol    ) {
        this.symbol = symbol;
    }


    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public adt_Equation getAdt_equation() {
        return adt_equation;
    }

    public void setAdt_equation(adt_Equation adt_equation) {
        this.adt_equation = adt_equation;
    }
    public adt_ASort getAdt_asort() {
        return adt_asort;
    }

    public void setAdt_asort(adt_ASort adt_asort) {
        this.adt_asort = adt_asort;
    }
    public adt_ADT getAdt_adt() {
        return adt_adt;
    }

    public void setAdt_adt(adt_ADT adt_adt) {
        this.adt_adt = adt_adt;
    }
    public adt_Equation getAdt_equation() {
        return adt_equation;
    }

    public void setAdt_equation(adt_Equation adt_equation) {
        this.adt_equation = adt_equation;
    }

}