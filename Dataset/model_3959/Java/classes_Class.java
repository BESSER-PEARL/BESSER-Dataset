





import java.util.List;
import java.util.ArrayList;

public class classes_Class extends Classifier {

    private boolean active;





    private List<classes_Property> classes_propertys;




    private classes_Property classes_property;




    private List<classes_Class> classes_classs;




    private List<classes_Classifier> classes_classifiers;


    public classes_Class(
        boolean active    ) {
        super(
        );
        this.active = active;
        this.classes_propertys = new ArrayList<>();
        this.classes_classs = new ArrayList<>();
        this.classes_classifiers = new ArrayList<>();
    }

    public classes_Class(
        boolean active        ArrayList<classes_Property> classes_propertys,        ArrayList<classes_Class> classes_classs,        ArrayList<classes_Classifier> classes_classifiers    ) {
        this.active = active;
        this.classes_propertys = classes_propertys;
        this.classes_classs = classes_classs;
        this.classes_classifiers = classes_classifiers;
    }

    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public List<classes_Property> getClasses_propertys() {
        return classes_propertys;
    }

    public void addClasses_property(Classes_property classes_property) {
        this.classes_propertys.add(classes_property);
    }
    public classes_Property getClasses_property() {
        return classes_property;
    }

    public void setClasses_property(classes_Property classes_property) {
        this.classes_property = classes_property;
    }
    public List<classes_Class> getClasses_classs() {
        return classes_classs;
    }

    public void addClasses_class(Classes_class classes_class) {
        this.classes_classs.add(classes_class);
    }
    public List<classes_Classifier> getClasses_classifiers() {
        return classes_classifiers;
    }

    public void addClasses_classifier(Classes_classifier classes_classifier) {
        this.classes_classifiers.add(classes_classifier);
    }

}