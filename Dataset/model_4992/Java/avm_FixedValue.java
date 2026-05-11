





import java.util.List;
import java.util.ArrayList;

public class avm_FixedValue extends ValueExpressionType {

    private String Value;
    private String Uncertainty;



    public avm_FixedValue(
        String Value,        String Uncertainty    ) {
        super(
        );
        this.Value = Value;
        this.Uncertainty = Uncertainty;
    }


    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getUncertainty() {
        return Uncertainty;
    }

    public void setUncertainty(String Uncertainty) {
        this.Uncertainty = Uncertainty;
    }


}