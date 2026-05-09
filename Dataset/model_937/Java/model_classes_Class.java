





import java.util.List;
import java.util.ArrayList;

public class model_classes_Class extends PackageElement {






    private List<classes_Attribute> classes_attributes;




    private List<classes_Class> classes_classs;




    private List<classes_Method> classes_methods;




    private List<requirement_Scenario> requirement_scenarios;




    private List<classes_Class> classes_classs;




    private List<classes_Association> classes_associations;




    private List<requirement_UseCase> requirement_usecases;




    private List<classes_Association> classes_associations;


    public model_classes_Class(
    ) {
        super(
        );
        this.classes_attributes = new ArrayList<>();
        this.classes_classs = new ArrayList<>();
        this.classes_methods = new ArrayList<>();
        this.requirement_scenarios = new ArrayList<>();
        this.classes_classs = new ArrayList<>();
        this.classes_associations = new ArrayList<>();
        this.requirement_usecases = new ArrayList<>();
        this.classes_associations = new ArrayList<>();
    }

    public model_classes_Class(
        ArrayList<classes_Attribute> classes_attributes,        ArrayList<classes_Class> classes_classs,        ArrayList<classes_Method> classes_methods,        ArrayList<requirement_Scenario> requirement_scenarios,        ArrayList<classes_Class> classes_classs,        ArrayList<classes_Association> classes_associations,        ArrayList<requirement_UseCase> requirement_usecases,        ArrayList<classes_Association> classes_associations    ) {
        this.classes_attributes = classes_attributes;
        this.classes_classs = classes_classs;
        this.classes_methods = classes_methods;
        this.requirement_scenarios = requirement_scenarios;
        this.classes_classs = classes_classs;
        this.classes_associations = classes_associations;
        this.requirement_usecases = requirement_usecases;
        this.classes_associations = classes_associations;
    }


    public List<classes_Attribute> getClasses_attributes() {
        return classes_attributes;
    }

    public void addClasses_attribute(Classes_attribute classes_attribute) {
        this.classes_attributes.add(classes_attribute);
    }
    public List<classes_Class> getClasses_classs() {
        return classes_classs;
    }

    public void addClasses_class(Classes_class classes_class) {
        this.classes_classs.add(classes_class);
    }
    public List<classes_Method> getClasses_methods() {
        return classes_methods;
    }

    public void addClasses_method(Classes_method classes_method) {
        this.classes_methods.add(classes_method);
    }
    public List<requirement_Scenario> getRequirement_scenarios() {
        return requirement_scenarios;
    }

    public void addRequirement_scenario(Requirement_scenario requirement_scenario) {
        this.requirement_scenarios.add(requirement_scenario);
    }
    public List<classes_Class> getClasses_classs() {
        return classes_classs;
    }

    public void addClasses_class(Classes_class classes_class) {
        this.classes_classs.add(classes_class);
    }
    public List<classes_Association> getClasses_associations() {
        return classes_associations;
    }

    public void addClasses_association(Classes_association classes_association) {
        this.classes_associations.add(classes_association);
    }
    public List<requirement_UseCase> getRequirement_usecases() {
        return requirement_usecases;
    }

    public void addRequirement_usecase(Requirement_usecase requirement_usecase) {
        this.requirement_usecases.add(requirement_usecase);
    }
    public List<classes_Association> getClasses_associations() {
        return classes_associations;
    }

    public void addClasses_association(Classes_association classes_association) {
        this.classes_associations.add(classes_association);
    }

}