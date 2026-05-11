





import java.util.List;
import java.util.ArrayList;

public class aml_ProductPUIDFeature  {

    private String name;
    private int values;





    private aml_MinMax aml_minmax;


    public aml_ProductPUIDFeature(
        String name,        int values    ) {
        this.name = name;
        this.values = values;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getValues() {
        return values;
    }

    public void setValues(int values) {
        this.values = values;
    }

    public aml_MinMax getAml_minmax() {
        return aml_minmax;
    }

    public void setAml_minmax(aml_MinMax aml_minmax) {
        this.aml_minmax = aml_minmax;
    }

}