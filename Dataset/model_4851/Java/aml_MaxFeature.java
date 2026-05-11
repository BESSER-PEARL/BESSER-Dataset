





import java.util.List;
import java.util.ArrayList;

public class aml_MaxFeature  {

    private int value;
    private String name;





    private aml_MinMax aml_minmax;


    public aml_MaxFeature(
        int value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
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