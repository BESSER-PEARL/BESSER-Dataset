





import java.util.List;
import java.util.ArrayList;

public class aml_TypeFeature  {

    private String value;
    private String name;





    private aml_Drive aml_drive;


    public aml_TypeFeature(
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

    public aml_Drive getAml_drive() {
        return aml_drive;
    }

    public void setAml_drive(aml_Drive aml_drive) {
        this.aml_drive = aml_drive;
    }

}