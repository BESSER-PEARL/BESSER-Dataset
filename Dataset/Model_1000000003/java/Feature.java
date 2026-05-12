





import java.util.List;
import java.util.ArrayList;

public class Feature extends Element {

    private String feature_type;
    private float min_value;
    private float max_value;





    private Datashape datashape;




    private List<Datashape> datashapes;


    public Feature(
        String feature_type,        float min_value,        float max_value    ) {
        super(
        );
        this.feature_type = feature_type;
        this.min_value = min_value;
        this.max_value = max_value;
        this.datashapes = new ArrayList<>();
    }

    public Feature(
        String feature_type,        float min_value,        float max_value        ArrayList<Datashape> datashapes    ) {
        this.feature_type = feature_type;
        this.min_value = min_value;
        this.max_value = max_value;
        this.datashapes = datashapes;
    }

    public String getFeature_type() {
        return feature_type;
    }

    public void setFeature_type(String feature_type) {
        this.feature_type = feature_type;
    }
    public float getMin_value() {
        return min_value;
    }

    public void setMin_value(float min_value) {
        this.min_value = min_value;
    }
    public float getMax_value() {
        return max_value;
    }

    public void setMax_value(float max_value) {
        this.max_value = max_value;
    }

    public Datashape getDatashape() {
        return datashape;
    }

    public void setDatashape(Datashape datashape) {
        this.datashape = datashape;
    }
    public List<Datashape> getDatashapes() {
        return datashapes;
    }

    public void addDatashape(Datashape datashape) {
        this.datashapes.add(datashape);
    }

}