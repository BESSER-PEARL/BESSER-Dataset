





import java.util.List;
import java.util.ArrayList;

public class cmof_Classifier extends Type, RedefinableElement, Namespace {

    private String isFinalSpecialization;
    private String isAbstract;





    private cmof_Class cmof_class;




    private cmof_Feature cmof_feature;




    private List<cmof_Property> cmof_propertys;




    private cmof_Classifier cmof_classifier;




    private List<cmof_NamedElement> cmof_namedelements;




    private List<cmof_Feature> cmof_features;




    private cmof_Classifier cmof_classifier;


    public cmof_Classifier(
        String isFinalSpecialization,        String isAbstract    ) {
        super(
        );
        this.isFinalSpecialization = isFinalSpecialization;
        this.isAbstract = isAbstract;
        this.cmof_propertys = new ArrayList<>();
        this.cmof_namedelements = new ArrayList<>();
        this.cmof_features = new ArrayList<>();
    }

    public cmof_Classifier(
        String isFinalSpecialization,        String isAbstract        ArrayList<cmof_Property> cmof_propertys,        ArrayList<cmof_NamedElement> cmof_namedelements,        ArrayList<cmof_Feature> cmof_features    ) {
        this.isFinalSpecialization = isFinalSpecialization;
        this.isAbstract = isAbstract;
        this.cmof_propertys = cmof_propertys;
        this.cmof_namedelements = cmof_namedelements;
        this.cmof_features = cmof_features;
    }

    public String getIsfinalspecialization() {
        return isFinalSpecialization;
    }

    public void setIsfinalspecialization(String isFinalSpecialization) {
        this.isFinalSpecialization = isFinalSpecialization;
    }
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public cmof_Class getCmof_class() {
        return cmof_class;
    }

    public void setCmof_class(cmof_Class cmof_class) {
        this.cmof_class = cmof_class;
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
    public cmof_Classifier getCmof_classifier() {
        return cmof_classifier;
    }

    public void setCmof_classifier(cmof_Classifier cmof_classifier) {
        this.cmof_classifier = cmof_classifier;
    }
    public List<cmof_NamedElement> getCmof_namedelements() {
        return cmof_namedelements;
    }

    public void addCmof_namedelement(Cmof_namedelement cmof_namedelement) {
        this.cmof_namedelements.add(cmof_namedelement);
    }
    public List<cmof_Feature> getCmof_features() {
        return cmof_features;
    }

    public void addCmof_feature(Cmof_feature cmof_feature) {
        this.cmof_features.add(cmof_feature);
    }
    public cmof_Classifier getCmof_classifier() {
        return cmof_classifier;
    }

    public void setCmof_classifier(cmof_Classifier cmof_classifier) {
        this.cmof_classifier = cmof_classifier;
    }

}