





import java.util.List;
import java.util.ArrayList;

public class vcml_Option  {

    private String name;
    private String value;





    private vcml_VcmlModel vcml_vcmlmodel;


    public vcml_Option(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public vcml_VcmlModel getVcml_vcmlmodel() {
        return vcml_vcmlmodel;
    }

    public void setVcml_vcmlmodel(vcml_VcmlModel vcml_vcmlmodel) {
        this.vcml_vcmlmodel = vcml_vcmlmodel;
    }

}