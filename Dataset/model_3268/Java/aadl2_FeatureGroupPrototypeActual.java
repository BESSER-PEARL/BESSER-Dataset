





import java.util.List;
import java.util.ArrayList;

public class aadl2_FeatureGroupPrototypeActual extends FeaturePrototypeActual {






    private List<aadl2_PrototypeBinding> aadl2_prototypebindings;




    private aadl2_FeatureType aadl2_featuretype;




    private aadl2_FeatureGroupPrototypeBinding aadl2_featuregroupprototypebinding;


    public aadl2_FeatureGroupPrototypeActual(
    ) {
        super(
        );
        this.aadl2_prototypebindings = new ArrayList<>();
    }

    public aadl2_FeatureGroupPrototypeActual(
        ArrayList<aadl2_PrototypeBinding> aadl2_prototypebindings    ) {
        this.aadl2_prototypebindings = aadl2_prototypebindings;
    }


    public List<aadl2_PrototypeBinding> getAadl2_prototypebindings() {
        return aadl2_prototypebindings;
    }

    public void addAadl2_prototypebinding(Aadl2_prototypebinding aadl2_prototypebinding) {
        this.aadl2_prototypebindings.add(aadl2_prototypebinding);
    }
    public aadl2_FeatureType getAadl2_featuretype() {
        return aadl2_featuretype;
    }

    public void setAadl2_featuretype(aadl2_FeatureType aadl2_featuretype) {
        this.aadl2_featuretype = aadl2_featuretype;
    }
    public aadl2_FeatureGroupPrototypeBinding getAadl2_featuregroupprototypebinding() {
        return aadl2_featuregroupprototypebinding;
    }

    public void setAadl2_featuregroupprototypebinding(aadl2_FeatureGroupPrototypeBinding aadl2_featuregroupprototypebinding) {
        this.aadl2_featuregroupprototypebinding = aadl2_featuregroupprototypebinding;
    }

}