





import java.util.List;
import java.util.ArrayList;

public class ccore_Page  {

    private String description;
    private String idRuntime;
    private String title;
    private String label;





    private ccore_TypeDefinition ccore_typedefinition;




    private ccore_TypeDefinition ccore_typedefinition;




    private List<ccore_Attribute> ccore_attributes;




    private ccore_Page ccore_page;


    public ccore_Page(
        String description,        String idRuntime,        String title,        String label    ) {
        this.description = description;
        this.idRuntime = idRuntime;
        this.title = title;
        this.label = label;
        this.ccore_attributes = new ArrayList<>();
    }

    public ccore_Page(
        String description,        String idRuntime,        String title,        String label        ArrayList<ccore_Attribute> ccore_attributes    ) {
        this.description = description;
        this.idRuntime = idRuntime;
        this.title = title;
        this.label = label;
        this.ccore_attributes = ccore_attributes;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getIdruntime() {
        return idRuntime;
    }

    public void setIdruntime(String idRuntime) {
        this.idRuntime = idRuntime;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public ccore_TypeDefinition getCcore_typedefinition() {
        return ccore_typedefinition;
    }

    public void setCcore_typedefinition(ccore_TypeDefinition ccore_typedefinition) {
        this.ccore_typedefinition = ccore_typedefinition;
    }
    public ccore_TypeDefinition getCcore_typedefinition() {
        return ccore_typedefinition;
    }

    public void setCcore_typedefinition(ccore_TypeDefinition ccore_typedefinition) {
        this.ccore_typedefinition = ccore_typedefinition;
    }
    public List<ccore_Attribute> getCcore_attributes() {
        return ccore_attributes;
    }

    public void addCcore_attribute(Ccore_attribute ccore_attribute) {
        this.ccore_attributes.add(ccore_attribute);
    }
    public ccore_Page getCcore_page() {
        return ccore_page;
    }

    public void setCcore_page(ccore_Page ccore_page) {
        this.ccore_page = ccore_page;
    }

}