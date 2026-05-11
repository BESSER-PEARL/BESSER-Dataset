





import java.util.List;
import java.util.ArrayList;

public class fmp_Feature extends Clonable {

    private String name;
    private String valueType;





    private List<fmp_Feature> fmp_features;


    public fmp_Feature(
        String name,        String valueType    ) {
        super(
        );
        this.name = name;
        this.valueType = valueType;
        this.fmp_features = new ArrayList<>();
    }

    public fmp_Feature(
        String name,        String valueType        ArrayList<fmp_Feature> fmp_features    ) {
        this.name = name;
        this.valueType = valueType;
        this.fmp_features = fmp_features;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValuetype() {
        return valueType;
    }

    public void setValuetype(String valueType) {
        this.valueType = valueType;
    }

    public List<fmp_Feature> getFmp_features() {
        return fmp_features;
    }

    public void addFmp_feature(Fmp_feature fmp_feature) {
        this.fmp_features.add(fmp_feature);
    }

}