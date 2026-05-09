





import java.util.List;
import java.util.ArrayList;

public class rapidml_ObjectRealization extends Extensible {






    private rapidml_RealizationContainer rapidml_realizationcontainer;




    private List<rapidml_Feature> rapidml_features;




    private rapidml_RealizationContainer rapidml_realizationcontainer;




    private rapidml_RealizationContainer rapidml_realizationcontainer;


    public rapidml_ObjectRealization(
    ) {
        super(
        );
        this.rapidml_features = new ArrayList<>();
    }

    public rapidml_ObjectRealization(
        ArrayList<rapidml_Feature> rapidml_features    ) {
        this.rapidml_features = rapidml_features;
    }


    public rapidml_RealizationContainer getRapidml_realizationcontainer() {
        return rapidml_realizationcontainer;
    }

    public void setRapidml_realizationcontainer(rapidml_RealizationContainer rapidml_realizationcontainer) {
        this.rapidml_realizationcontainer = rapidml_realizationcontainer;
    }
    public List<rapidml_Feature> getRapidml_features() {
        return rapidml_features;
    }

    public void addRapidml_feature(Rapidml_feature rapidml_feature) {
        this.rapidml_features.add(rapidml_feature);
    }
    public rapidml_RealizationContainer getRapidml_realizationcontainer() {
        return rapidml_realizationcontainer;
    }

    public void setRapidml_realizationcontainer(rapidml_RealizationContainer rapidml_realizationcontainer) {
        this.rapidml_realizationcontainer = rapidml_realizationcontainer;
    }
    public rapidml_RealizationContainer getRapidml_realizationcontainer() {
        return rapidml_realizationcontainer;
    }

    public void setRapidml_realizationcontainer(rapidml_RealizationContainer rapidml_realizationcontainer) {
        this.rapidml_realizationcontainer = rapidml_realizationcontainer;
    }

}