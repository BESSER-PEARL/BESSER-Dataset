





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Class extends Classifier {

    private String isActive;





    private List<RefOntoUML_Class> refontouml_classs;




    private List<RefOntoUML_Classifier> refontouml_classifiers;




    private List<RefOntoUML_Property> refontouml_propertys;




    private RefOntoUML_Property refontouml_property;


    public RefOntoUML_Class(
        String isActive    ) {
        super(
        );
        this.isActive = isActive;
        this.refontouml_classs = new ArrayList<>();
        this.refontouml_classifiers = new ArrayList<>();
        this.refontouml_propertys = new ArrayList<>();
    }

    public RefOntoUML_Class(
        String isActive        ArrayList<RefOntoUML_Class> refontouml_classs,        ArrayList<RefOntoUML_Classifier> refontouml_classifiers,        ArrayList<RefOntoUML_Property> refontouml_propertys    ) {
        this.isActive = isActive;
        this.refontouml_classs = refontouml_classs;
        this.refontouml_classifiers = refontouml_classifiers;
        this.refontouml_propertys = refontouml_propertys;
    }

    public String getIsactive() {
        return isActive;
    }

    public void setIsactive(String isActive) {
        this.isActive = isActive;
    }

    public List<RefOntoUML_Class> getRefontouml_classs() {
        return refontouml_classs;
    }

    public void addRefontouml_class(Refontouml_class refontouml_class) {
        this.refontouml_classs.add(refontouml_class);
    }
    public List<RefOntoUML_Classifier> getRefontouml_classifiers() {
        return refontouml_classifiers;
    }

    public void addRefontouml_classifier(Refontouml_classifier refontouml_classifier) {
        this.refontouml_classifiers.add(refontouml_classifier);
    }
    public List<RefOntoUML_Property> getRefontouml_propertys() {
        return refontouml_propertys;
    }

    public void addRefontouml_property(Refontouml_property refontouml_property) {
        this.refontouml_propertys.add(refontouml_property);
    }
    public RefOntoUML_Property getRefontouml_property() {
        return refontouml_property;
    }

    public void setRefontouml_property(RefOntoUML_Property refontouml_property) {
        this.refontouml_property = refontouml_property;
    }

}