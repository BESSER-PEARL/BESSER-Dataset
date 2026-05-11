





import java.util.List;
import java.util.ArrayList;

public class aml_CreatingTool  {

    private String label;
    private String version;
    private String toolType;





    private aml_Template aml_template;




    private aml_Argument aml_argument;




    private aml_Collection aml_collection;


    public aml_CreatingTool(
        String label,        String version,        String toolType    ) {
        this.label = label;
        this.version = version;
        this.toolType = toolType;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getTooltype() {
        return toolType;
    }

    public void setTooltype(String toolType) {
        this.toolType = toolType;
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
    public aml_Collection getAml_collection() {
        return aml_collection;
    }

    public void setAml_collection(aml_Collection aml_collection) {
        this.aml_collection = aml_collection;
    }

}