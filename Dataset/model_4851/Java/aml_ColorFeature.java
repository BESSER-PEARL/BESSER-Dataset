





import java.util.List;
import java.util.ArrayList;

public class aml_ColorFeature  {

    private String value;
    private String name;





    private aml_Cable aml_cable;


    public aml_ColorFeature(
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

    public aml_Cable getAml_cable() {
        return aml_cable;
    }

    public void setAml_cable(aml_Cable aml_cable) {
        this.aml_cable = aml_cable;
    }

}