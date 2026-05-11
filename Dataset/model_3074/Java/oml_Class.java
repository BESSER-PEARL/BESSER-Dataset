





import java.util.List;
import java.util.ArrayList;

public class oml_Class extends Classifier {

    private String isAbstract;





    private oml_Class oml_class;




    private List<oml_Feature> oml_features;




    private oml_Feature oml_feature;




    private oml_Class oml_class;


    public oml_Class(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.oml_features = new ArrayList<>();
    }

    public oml_Class(
        String isAbstract        ArrayList<oml_Feature> oml_features    ) {
        this.isAbstract = isAbstract;
        this.oml_features = oml_features;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public oml_Class getOml_class() {
        return oml_class;
    }

    public void setOml_class(oml_Class oml_class) {
        this.oml_class = oml_class;
    }
    public List<oml_Feature> getOml_features() {
        return oml_features;
    }

    public void addOml_feature(Oml_feature oml_feature) {
        this.oml_features.add(oml_feature);
    }
    public oml_Feature getOml_feature() {
        return oml_feature;
    }

    public void setOml_feature(oml_Feature oml_feature) {
        this.oml_feature = oml_feature;
    }
    public oml_Class getOml_class() {
        return oml_class;
    }

    public void setOml_class(oml_Class oml_class) {
        this.oml_class = oml_class;
    }

}