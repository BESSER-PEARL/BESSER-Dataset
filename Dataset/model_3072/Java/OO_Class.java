





import java.util.List;
import java.util.ArrayList;

public class OO_Class extends Classifier {

    private String isAbstract;





    private OO_Class oo_class;




    private List<OO_Class> oo_classs;




    private List<OO_Feature> oo_features;




    private OO_Feature oo_feature;


    public OO_Class(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.oo_classs = new ArrayList<>();
        this.oo_features = new ArrayList<>();
    }

    public OO_Class(
        String isAbstract        ArrayList<OO_Class> oo_classs,        ArrayList<OO_Feature> oo_features    ) {
        this.isAbstract = isAbstract;
        this.oo_classs = oo_classs;
        this.oo_features = oo_features;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public OO_Class getOo_class() {
        return oo_class;
    }

    public void setOo_class(OO_Class oo_class) {
        this.oo_class = oo_class;
    }
    public List<OO_Class> getOo_classs() {
        return oo_classs;
    }

    public void addOo_class(Oo_class oo_class) {
        this.oo_classs.add(oo_class);
    }
    public List<OO_Feature> getOo_features() {
        return oo_features;
    }

    public void addOo_feature(Oo_feature oo_feature) {
        this.oo_features.add(oo_feature);
    }
    public OO_Feature getOo_feature() {
        return oo_feature;
    }

    public void setOo_feature(OO_Feature oo_feature) {
        this.oo_feature = oo_feature;
    }

}