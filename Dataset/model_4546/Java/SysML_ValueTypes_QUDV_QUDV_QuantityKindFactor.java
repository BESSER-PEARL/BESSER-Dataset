





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor  {

    private String name;





    private Rational rational;




    private QuantityKind quantitykind;


    public SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Rational getRational() {
        return rational;
    }

    public void setRational(Rational rational) {
        this.rational = rational;
    }
    public QuantityKind getQuantitykind() {
        return quantitykind;
    }

    public void setQuantitykind(QuantityKind quantitykind) {
        this.quantitykind = quantitykind;
    }

}