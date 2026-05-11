





import java.util.List;
import java.util.ArrayList;

public class viewpoint_validation_ValidationSet extends DocumentedElement {

    private String name;





    private List<validation_ValidationRule> validation_validationrules;




    private List<validation_ValidationRule> validation_validationrules;




    private List<validation_ValidationRule> validation_validationrules;


    public viewpoint_validation_ValidationSet(
        String name    ) {
        super(
        );
        this.name = name;
        this.validation_validationrules = new ArrayList<>();
        this.validation_validationrules = new ArrayList<>();
        this.validation_validationrules = new ArrayList<>();
    }

    public viewpoint_validation_ValidationSet(
        String name        ArrayList<validation_ValidationRule> validation_validationrules,        ArrayList<validation_ValidationRule> validation_validationrules,        ArrayList<validation_ValidationRule> validation_validationrules    ) {
        this.name = name;
        this.validation_validationrules = validation_validationrules;
        this.validation_validationrules = validation_validationrules;
        this.validation_validationrules = validation_validationrules;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<validation_ValidationRule> getValidation_validationrules() {
        return validation_validationrules;
    }

    public void addValidation_validationrule(Validation_validationrule validation_validationrule) {
        this.validation_validationrules.add(validation_validationrule);
    }
    public List<validation_ValidationRule> getValidation_validationrules() {
        return validation_validationrules;
    }

    public void addValidation_validationrule(Validation_validationrule validation_validationrule) {
        this.validation_validationrules.add(validation_validationrule);
    }
    public List<validation_ValidationRule> getValidation_validationrules() {
        return validation_validationrules;
    }

    public void addValidation_validationrule(Validation_validationrule validation_validationrule) {
        this.validation_validationrules.add(validation_validationrule);
    }

}