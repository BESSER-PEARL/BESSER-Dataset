





import java.util.List;
import java.util.ArrayList;

public class myDsl_Entity  {

    private String name;





    private myDsl_Model mydsl_model;




    private List<myDsl_Feature> mydsl_features;


    public myDsl_Entity(
        String name    ) {
        this.name = name;
        this.mydsl_features = new ArrayList<>();
    }

    public myDsl_Entity(
        String name        ArrayList<myDsl_Feature> mydsl_features    ) {
        this.name = name;
        this.mydsl_features = mydsl_features;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_Model getMydsl_model() {
        return mydsl_model;
    }

    public void setMydsl_model(myDsl_Model mydsl_model) {
        this.mydsl_model = mydsl_model;
    }
    public List<myDsl_Feature> getMydsl_features() {
        return mydsl_features;
    }

    public void addMydsl_feature(Mydsl_feature mydsl_feature) {
        this.mydsl_features.add(mydsl_feature);
    }

}