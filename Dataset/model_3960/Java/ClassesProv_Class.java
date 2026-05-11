





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_Class extends Classifier {






    private ClassesProv_Property classesprov_property;




    private ClassesProv_Class classesprov_class;




    private List<ClassesProv_Classifier> classesprov_classifiers;




    private List<ClassesProv_Property> classesprov_propertys;


    public ClassesProv_Class(
    ) {
        super(
        );
        this.classesprov_classifiers = new ArrayList<>();
        this.classesprov_propertys = new ArrayList<>();
    }

    public ClassesProv_Class(
        ArrayList<ClassesProv_Classifier> classesprov_classifiers,        ArrayList<ClassesProv_Property> classesprov_propertys    ) {
        this.classesprov_classifiers = classesprov_classifiers;
        this.classesprov_propertys = classesprov_propertys;
    }


    public ClassesProv_Property getClassesprov_property() {
        return classesprov_property;
    }

    public void setClassesprov_property(ClassesProv_Property classesprov_property) {
        this.classesprov_property = classesprov_property;
    }
    public ClassesProv_Class getClassesprov_class() {
        return classesprov_class;
    }

    public void setClassesprov_class(ClassesProv_Class classesprov_class) {
        this.classesprov_class = classesprov_class;
    }
    public List<ClassesProv_Classifier> getClassesprov_classifiers() {
        return classesprov_classifiers;
    }

    public void addClassesprov_classifier(Classesprov_classifier classesprov_classifier) {
        this.classesprov_classifiers.add(classesprov_classifier);
    }
    public List<ClassesProv_Property> getClassesprov_propertys() {
        return classesprov_propertys;
    }

    public void addClassesprov_property(Classesprov_property classesprov_property) {
        this.classesprov_propertys.add(classesprov_property);
    }

}