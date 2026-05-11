





import java.util.List;
import java.util.ArrayList;

public class aml_TargetGroupFeature  {

    private String value;
    private String name;





    private aml_MinMax aml_minmax;


    public aml_TargetGroupFeature(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public aml_MinMax getAml_minmax() {
        return aml_minmax;
    }

    public void setAml_minmax(aml_MinMax aml_minmax) {
        this.aml_minmax = aml_minmax;
    }

}