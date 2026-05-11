





import java.util.List;
import java.util.ArrayList;

public class cmof_Classifier extends Namespace, RedefinableElement, Type {

    private String isAbstract;
    private String isFinalSpecialization;





    private cmof_Feature cmof_feature;




    private List<cmof_Property> cmof_propertys;




    private List<cmof_Classifier> cmof_classifiers;




    private cmof_Classifier cmof_classifier;




    private List<cmof_Feature> cmof_features;




    private cmof_Class cmof_class;


    public cmof_Classifier(
        String isAbstract,        String isFinalSpecialization    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.isFinalSpecialization = isFinalSpecialization;
        this.cmof_propertys = new ArrayList<>();
        this.cmof_classifiers = new ArrayList<>();
        this.cmof_features = new ArrayList<>();
    }

    public cmof_Classifier(
        String isAbstract,        String isFinalSpecialization        ArrayList<cmof_Property> cmof_propertys,        ArrayList<cmof_Classifier> cmof_classifiers,        ArrayList<cmof_Feature> cmof_features    ) {
        this.isAbstract = isAbstract;
        this.isFinalSpecialization = isFinalSpecialization;
        this.cmof_propertys = cmof_propertys;
        this.cmof_classifiers = cmof_classifiers;
        this.cmof_features = cmof_features;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getIsfinalspecialization() {
        return isFinalSpecialization;
    }

    public void setIsfinalspecialization(String isFinalSpecialization) {
        this.isFinalSpecialization = isFinalSpecialization;
    }

    public cmof_Feature getCmof_feature() {
        return cmof_feature;
    }

    public void setCmof_feature(cmof_Feature cmof_feature) {
        this.cmof_feature = cmof_feature;
    }
    public List<cmof_Property> getCmof_propertys() {
        return cmof_propertys;
    }

    public void addCmof_property(Cmof_property cmof_property) {
        this.cmof_propertys.add(cmof_property);
    }
    public List<cmof_Classifier> getCmof_classifiers() {
        return cmof_classifiers;
    }

    public void addCmof_classifier(Cmof_classifier cmof_classifier) {
        this.cmof_classifiers.add(cmof_classifier);
    }
    public cmof_Classifier getCmof_classifier() {
        return cmof_classifier;
    }

    public void setCmof_classifier(cmof_Classifier cmof_classifier) {
        this.cmof_classifier = cmof_classifier;
    }
    public List<cmof_Feature> getCmof_features() {
        return cmof_features;
    }

    public void addCmof_feature(Cmof_feature cmof_feature) {
        this.cmof_features.add(cmof_feature);
    }
    public cmof_Class getCmof_class() {
        return cmof_class;
    }

    public void setCmof_class(cmof_Class cmof_class) {
        this.cmof_class = cmof_class;
    }

}