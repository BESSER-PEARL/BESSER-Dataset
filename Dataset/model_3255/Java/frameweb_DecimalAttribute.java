





import java.util.List;
import java.util.ArrayList;

public class frameweb_DecimalAttribute extends DomainAttribute {

    private String decimalScale;
    private String decimalPrecision;



    public frameweb_DecimalAttribute(
        String decimalScale,        String decimalPrecision    ) {
        super(
        );
        this.decimalScale = decimalScale;
        this.decimalPrecision = decimalPrecision;
    }


    public String getDecimalscale() {
        return decimalScale;
    }

    public void setDecimalscale(String decimalScale) {
        this.decimalScale = decimalScale;
    }
    public String getDecimalprecision() {
        return decimalPrecision;
    }

    public void setDecimalprecision(String decimalPrecision) {
        this.decimalPrecision = decimalPrecision;
    }


}