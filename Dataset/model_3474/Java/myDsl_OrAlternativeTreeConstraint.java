





import java.util.List;
import java.util.ArrayList;

public class myDsl_OrAlternativeTreeConstraint extends TreeConstraint {

    private int max;
    private int min;





    private List<myDsl_Feature> mydsl_features;


    public myDsl_OrAlternativeTreeConstraint(
        int max,        int min    ) {
        super(
        );
        this.max = max;
        this.min = min;
        this.mydsl_features = new ArrayList<>();
    }

    public myDsl_OrAlternativeTreeConstraint(
        int max,        int min        ArrayList<myDsl_Feature> mydsl_features    ) {
        this.max = max;
        this.min = min;
        this.mydsl_features = mydsl_features;
    }

    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }
    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }

    public List<myDsl_Feature> getMydsl_features() {
        return mydsl_features;
    }

    public void addMydsl_feature(Mydsl_feature mydsl_feature) {
        this.mydsl_features.add(mydsl_feature);
    }

}