





import java.util.List;
import java.util.ArrayList;

public class sgen_FeatureParameter extends NamedElement, DeprecatableElement {

    private String parameterType;
    private boolean optional;





    private sgen_FeatureType sgen_featuretype;




    private sgen_FeatureType sgen_featuretype;




    private sgen_FeatureParameterValue sgen_featureparametervalue;


    public sgen_FeatureParameter(
        String parameterType,        boolean optional    ) {
        super(
        );
        this.parameterType = parameterType;
        this.optional = optional;
    }


    public String getParametertype() {
        return parameterType;
    }

    public void setParametertype(String parameterType) {
        this.parameterType = parameterType;
    }
    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }

    public sgen_FeatureType getSgen_featuretype() {
        return sgen_featuretype;
    }

    public void setSgen_featuretype(sgen_FeatureType sgen_featuretype) {
        this.sgen_featuretype = sgen_featuretype;
    }
    public sgen_FeatureType getSgen_featuretype() {
        return sgen_featuretype;
    }

    public void setSgen_featuretype(sgen_FeatureType sgen_featuretype) {
        this.sgen_featuretype = sgen_featuretype;
    }
    public sgen_FeatureParameterValue getSgen_featureparametervalue() {
        return sgen_featureparametervalue;
    }

    public void setSgen_featureparametervalue(sgen_FeatureParameterValue sgen_featureparametervalue) {
        this.sgen_featureparametervalue = sgen_featureparametervalue;
    }

}