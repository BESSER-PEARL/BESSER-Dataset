





import java.util.List;
import java.util.ArrayList;

public class feature_HyVersion extends HyTemporalElement {

    private String number;





    private feature_HyVersion feature_hyversion;




    private feature_HyFeature feature_hyfeature;




    private feature_HyFeature feature_hyfeature;




    private List<feature_HyVersion> feature_hyversions;


    public feature_HyVersion(
        String number    ) {
        super(
        );
        this.number = number;
        this.feature_hyversions = new ArrayList<>();
    }

    public feature_HyVersion(
        String number        ArrayList<feature_HyVersion> feature_hyversions    ) {
        this.number = number;
        this.feature_hyversions = feature_hyversions;
    }

    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public feature_HyVersion getFeature_hyversion() {
        return feature_hyversion;
    }

    public void setFeature_hyversion(feature_HyVersion feature_hyversion) {
        this.feature_hyversion = feature_hyversion;
    }
    public feature_HyFeature getFeature_hyfeature() {
        return feature_hyfeature;
    }

    public void setFeature_hyfeature(feature_HyFeature feature_hyfeature) {
        this.feature_hyfeature = feature_hyfeature;
    }
    public feature_HyFeature getFeature_hyfeature() {
        return feature_hyfeature;
    }

    public void setFeature_hyfeature(feature_HyFeature feature_hyfeature) {
        this.feature_hyfeature = feature_hyfeature;
    }
    public List<feature_HyVersion> getFeature_hyversions() {
        return feature_hyversions;
    }

    public void addFeature_hyversion(Feature_hyversion feature_hyversion) {
        this.feature_hyversions.add(feature_hyversion);
    }

}