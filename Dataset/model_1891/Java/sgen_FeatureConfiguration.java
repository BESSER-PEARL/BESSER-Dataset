





import java.util.List;
import java.util.ArrayList;

public class sgen_FeatureConfiguration  {






    private sgen_FeatureParameterValue sgen_featureparametervalue;




    private sgen_GeneratorEntry sgen_generatorentry;




    private List<sgen_FeatureParameterValue> sgen_featureparametervalues;




    private sgen_GeneratorConfiguration sgen_generatorconfiguration;


    public sgen_FeatureConfiguration(
    ) {
        this.sgen_featureparametervalues = new ArrayList<>();
    }

    public sgen_FeatureConfiguration(
        ArrayList<sgen_FeatureParameterValue> sgen_featureparametervalues    ) {
        this.sgen_featureparametervalues = sgen_featureparametervalues;
    }


    public sgen_FeatureParameterValue getSgen_featureparametervalue() {
        return sgen_featureparametervalue;
    }

    public void setSgen_featureparametervalue(sgen_FeatureParameterValue sgen_featureparametervalue) {
        this.sgen_featureparametervalue = sgen_featureparametervalue;
    }
    public sgen_GeneratorEntry getSgen_generatorentry() {
        return sgen_generatorentry;
    }

    public void setSgen_generatorentry(sgen_GeneratorEntry sgen_generatorentry) {
        this.sgen_generatorentry = sgen_generatorentry;
    }
    public List<sgen_FeatureParameterValue> getSgen_featureparametervalues() {
        return sgen_featureparametervalues;
    }

    public void addSgen_featureparametervalue(Sgen_featureparametervalue sgen_featureparametervalue) {
        this.sgen_featureparametervalues.add(sgen_featureparametervalue);
    }
    public sgen_GeneratorConfiguration getSgen_generatorconfiguration() {
        return sgen_generatorconfiguration;
    }

    public void setSgen_generatorconfiguration(sgen_GeneratorConfiguration sgen_generatorconfiguration) {
        this.sgen_generatorconfiguration = sgen_generatorconfiguration;
    }

}