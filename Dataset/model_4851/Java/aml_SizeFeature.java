





import java.util.List;
import java.util.ArrayList;

public class aml_SizeFeature  {

    private String name;
    private int value;





    private aml_Drive aml_drive;


    public aml_SizeFeature(
        String name,        int value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public aml_Drive getAml_drive() {
        return aml_drive;
    }

    public void setAml_drive(aml_Drive aml_drive) {
        this.aml_drive = aml_drive;
    }

}