





import java.util.List;
import java.util.ArrayList;

public class becontent_Form extends FormElement {

    private String name;
    private String method;
    private String description;





    private becontent_DefinitionItem becontent_definitionitem;




    private becontent_EntityManagerPage becontent_entitymanagerpage;




    private List<becontent_Validation> becontent_validations;




    private List<becontent_FormElement> becontent_formelements;


    public becontent_Form(
        String name,        String method,        String description    ) {
        super(
        );
        this.name = name;
        this.method = method;
        this.description = description;
        this.becontent_validations = new ArrayList<>();
        this.becontent_formelements = new ArrayList<>();
    }

    public becontent_Form(
        String name,        String method,        String description        ArrayList<becontent_Validation> becontent_validations,        ArrayList<becontent_FormElement> becontent_formelements    ) {
        this.name = name;
        this.method = method;
        this.description = description;
        this.becontent_validations = becontent_validations;
        this.becontent_formelements = becontent_formelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public becontent_DefinitionItem getBecontent_definitionitem() {
        return becontent_definitionitem;
    }

    public void setBecontent_definitionitem(becontent_DefinitionItem becontent_definitionitem) {
        this.becontent_definitionitem = becontent_definitionitem;
    }
    public becontent_EntityManagerPage getBecontent_entitymanagerpage() {
        return becontent_entitymanagerpage;
    }

    public void setBecontent_entitymanagerpage(becontent_EntityManagerPage becontent_entitymanagerpage) {
        this.becontent_entitymanagerpage = becontent_entitymanagerpage;
    }
    public List<becontent_Validation> getBecontent_validations() {
        return becontent_validations;
    }

    public void addBecontent_validation(Becontent_validation becontent_validation) {
        this.becontent_validations.add(becontent_validation);
    }
    public List<becontent_FormElement> getBecontent_formelements() {
        return becontent_formelements;
    }

    public void addBecontent_formelement(Becontent_formelement becontent_formelement) {
        this.becontent_formelements.add(becontent_formelement);
    }

}