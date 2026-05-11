





import java.util.List;
import java.util.ArrayList;

public class aml_AbstractElements  {

    private String name;





    private aml_Aml aml_aml;


    public aml_AbstractElements(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public aml_Aml getAml_aml() {
        return aml_aml;
    }

    public void setAml_aml(aml_Aml aml_aml) {
        this.aml_aml = aml_aml;
    }

}