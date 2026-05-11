





import java.util.List;
import java.util.ArrayList;

public class aml_AmlDocument  {

    private String version;
    private String group;





    private List<aml_Template> aml_templates;




    private List<aml_Argument> aml_arguments;




    private List<aml_Exhibit> aml_exhibits;


    public aml_AmlDocument(
        String version,        String group    ) {
        this.version = version;
        this.group = group;
        this.aml_templates = new ArrayList<>();
        this.aml_arguments = new ArrayList<>();
        this.aml_exhibits = new ArrayList<>();
    }

    public aml_AmlDocument(
        String version,        String group        ArrayList<aml_Template> aml_templates,        ArrayList<aml_Argument> aml_arguments,        ArrayList<aml_Exhibit> aml_exhibits    ) {
        this.version = version;
        this.group = group;
        this.aml_templates = aml_templates;
        this.aml_arguments = aml_arguments;
        this.aml_exhibits = aml_exhibits;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<aml_Template> getAml_templates() {
        return aml_templates;
    }

    public void addAml_template(Aml_template aml_template) {
        this.aml_templates.add(aml_template);
    }
    public List<aml_Argument> getAml_arguments() {
        return aml_arguments;
    }

    public void addAml_argument(Aml_argument aml_argument) {
        this.aml_arguments.add(aml_argument);
    }
    public List<aml_Exhibit> getAml_exhibits() {
        return aml_exhibits;
    }

    public void addAml_exhibit(Aml_exhibit aml_exhibit) {
        this.aml_exhibits.add(aml_exhibit);
    }

}