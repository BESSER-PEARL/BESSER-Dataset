





import java.util.List;
import java.util.ArrayList;

public class gaml_Facet extends VarDefinition {

    private String key;





    private gaml_HeadlessExperiment gaml_headlessexperiment;


    public gaml_Facet(
        String key    ) {
        super(
        );
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public gaml_HeadlessExperiment getGaml_headlessexperiment() {
        return gaml_headlessexperiment;
    }

    public void setGaml_headlessexperiment(gaml_HeadlessExperiment gaml_headlessexperiment) {
        this.gaml_headlessexperiment = gaml_headlessexperiment;
    }

}