





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentType extends ComponentClassifier {

    private String noFeatures;





    private List<aadl2_Feature> aadl2_features;




    private aadl2_ComponentTypeRename aadl2_componenttyperename;




    private aadl2_ComponentType aadl2_componenttype;




    private aadl2_ComponentImplementation aadl2_componentimplementation;


    public aadl2_ComponentType(
        String noFeatures    ) {
        super(
        );
        this.noFeatures = noFeatures;
        this.aadl2_features = new ArrayList<>();
    }

    public aadl2_ComponentType(
        String noFeatures        ArrayList<aadl2_Feature> aadl2_features    ) {
        this.noFeatures = noFeatures;
        this.aadl2_features = aadl2_features;
    }

    public String getNofeatures() {
        return noFeatures;
    }

    public void setNofeatures(String noFeatures) {
        this.noFeatures = noFeatures;
    }

    public List<aadl2_Feature> getAadl2_features() {
        return aadl2_features;
    }

    public void addAadl2_feature(Aadl2_feature aadl2_feature) {
        this.aadl2_features.add(aadl2_feature);
    }
    public aadl2_ComponentTypeRename getAadl2_componenttyperename() {
        return aadl2_componenttyperename;
    }

    public void setAadl2_componenttyperename(aadl2_ComponentTypeRename aadl2_componenttyperename) {
        this.aadl2_componenttyperename = aadl2_componenttyperename;
    }
    public aadl2_ComponentType getAadl2_componenttype() {
        return aadl2_componenttype;
    }

    public void setAadl2_componenttype(aadl2_ComponentType aadl2_componenttype) {
        this.aadl2_componenttype = aadl2_componenttype;
    }
    public aadl2_ComponentImplementation getAadl2_componentimplementation() {
        return aadl2_componentimplementation;
    }

    public void setAadl2_componentimplementation(aadl2_ComponentImplementation aadl2_componentimplementation) {
        this.aadl2_componentimplementation = aadl2_componentimplementation;
    }

}