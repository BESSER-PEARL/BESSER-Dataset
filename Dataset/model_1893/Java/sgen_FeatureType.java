





import java.util.List;
import java.util.ArrayList;

public class sgen_FeatureType extends NamedElement, DeprecatableElement {

    private boolean optional;





    private sgen_FeatureConfiguration sgen_featureconfiguration;


    public sgen_FeatureType(
        boolean optional    ) {
        super(
        );
        this.optional = optional;
    }


    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }

    public sgen_FeatureConfiguration getSgen_featureconfiguration() {
        return sgen_featureconfiguration;
    }

    public void setSgen_featureconfiguration(sgen_FeatureConfiguration sgen_featureconfiguration) {
        this.sgen_featureconfiguration = sgen_featureconfiguration;
    }

}