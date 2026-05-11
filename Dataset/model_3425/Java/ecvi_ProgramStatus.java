





import java.util.List;
import java.util.ArrayList;

public class ecvi_ProgramStatus  {

    private String name;
    private String valueOther;
    private String value;





    private ecvi_Premises ecvi_premises;


    public ecvi_ProgramStatus(
        String name,        String valueOther,        String value    ) {
        this.name = name;
        this.valueOther = valueOther;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValueother() {
        return valueOther;
    }

    public void setValueother(String valueOther) {
        this.valueOther = valueOther;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public ecvi_Premises getEcvi_premises() {
        return ecvi_premises;
    }

    public void setEcvi_premises(ecvi_Premises ecvi_premises) {
        this.ecvi_premises = ecvi_premises;
    }

}