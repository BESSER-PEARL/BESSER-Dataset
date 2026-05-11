





import java.util.List;
import java.util.ArrayList;

public class aml_Coverage  {

    private String mixed;
    private String group;





    private aml_MetaData aml_metadata;


    public aml_Coverage(
        String mixed,        String group    ) {
        this.mixed = mixed;
        this.group = group;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public aml_MetaData getAml_metadata() {
        return aml_metadata;
    }

    public void setAml_metadata(aml_MetaData aml_metadata) {
        this.aml_metadata = aml_metadata;
    }

}