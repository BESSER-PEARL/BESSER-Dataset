





import java.util.List;
import java.util.ArrayList;

public class aml_Annotation  {

    private String mixed;
    private String id;
    private String group;





    private aml_Template aml_template;




    private aml_Argument aml_argument;




    private aml_DiscoveryMethod aml_discoverymethod;




    private aml_Exhibit aml_exhibit;


    public aml_Annotation(
        String mixed,        String id,        String group    ) {
        this.mixed = mixed;
        this.id = id;
        this.group = group;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public aml_Template getAml_template() {
        return aml_template;
    }

    public void setAml_template(aml_Template aml_template) {
        this.aml_template = aml_template;
    }
    public aml_Argument getAml_argument() {
        return aml_argument;
    }

    public void setAml_argument(aml_Argument aml_argument) {
        this.aml_argument = aml_argument;
    }
    public aml_DiscoveryMethod getAml_discoverymethod() {
        return aml_discoverymethod;
    }

    public void setAml_discoverymethod(aml_DiscoveryMethod aml_discoverymethod) {
        this.aml_discoverymethod = aml_discoverymethod;
    }
    public aml_Exhibit getAml_exhibit() {
        return aml_exhibit;
    }

    public void setAml_exhibit(aml_Exhibit aml_exhibit) {
        this.aml_exhibit = aml_exhibit;
    }

}