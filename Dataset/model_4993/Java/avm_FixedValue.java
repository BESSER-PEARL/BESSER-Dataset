





import java.util.List;
import java.util.ArrayList;

public class avm_FixedValue extends ValueExpressionType {

    private String Uncertainty;
    private String Value;



    public avm_FixedValue(
        String Uncertainty,        String Value    ) {
        super(
        );
        this.Uncertainty = Uncertainty;
        this.Value = Value;
    }


    public String getUncertainty() {
        return Uncertainty;
    }

    public void setUncertainty(String Uncertainty) {
        this.Uncertainty = Uncertainty;
    }
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }


}