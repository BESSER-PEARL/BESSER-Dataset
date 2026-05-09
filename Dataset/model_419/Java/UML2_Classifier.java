





import java.util.List;
import java.util.ArrayList;

public class UML2_Classifier extends Type, RedefinableElement, Namespace {

    private boolean isAbstract;





    private UML2_Feature uml2_feature;




    private List<UML2_Feature> uml2_features;


    public UML2_Classifier(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.uml2_features = new ArrayList<>();
    }

    public UML2_Classifier(
        boolean isAbstract        ArrayList<UML2_Feature> uml2_features    ) {
        this.isAbstract = isAbstract;
        this.uml2_features = uml2_features;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public UML2_Feature getUml2_feature() {
        return uml2_feature;
    }

    public void setUml2_feature(UML2_Feature uml2_feature) {
        this.uml2_feature = uml2_feature;
    }
    public List<UML2_Feature> getUml2_features() {
        return uml2_features;
    }

    public void addUml2_feature(Uml2_feature uml2_feature) {
        this.uml2_features.add(uml2_feature);
    }

}