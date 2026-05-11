





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_Rule  {

    private float conditionValue;
    private String conditionLiteral;





    private ioT_metamodel_Device iot_metamodel_device;


    public ioT_metamodel_Rule(
        float conditionValue,        String conditionLiteral    ) {
        this.conditionValue = conditionValue;
        this.conditionLiteral = conditionLiteral;
    }


    public float getConditionvalue() {
        return conditionValue;
    }

    public void setConditionvalue(float conditionValue) {
        this.conditionValue = conditionValue;
    }
    public String getConditionliteral() {
        return conditionLiteral;
    }

    public void setConditionliteral(String conditionLiteral) {
        this.conditionLiteral = conditionLiteral;
    }

    public ioT_metamodel_Device getIot_metamodel_device() {
        return iot_metamodel_device;
    }

    public void setIot_metamodel_device(ioT_metamodel_Device iot_metamodel_device) {
        this.iot_metamodel_device = iot_metamodel_device;
    }

}