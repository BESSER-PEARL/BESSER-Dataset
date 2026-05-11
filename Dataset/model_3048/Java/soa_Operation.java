





import java.util.List;
import java.util.ArrayList;

public class soa_Operation  {

    private String name;





    private List<soa_Exception> soa_exceptions;




    private List<soa_Feature> soa_features;




    private List<soa_Feature> soa_features;


    public soa_Operation(
        String name    ) {
        this.name = name;
        this.soa_exceptions = new ArrayList<>();
        this.soa_features = new ArrayList<>();
        this.soa_features = new ArrayList<>();
    }

    public soa_Operation(
        String name        ArrayList<soa_Exception> soa_exceptions,        ArrayList<soa_Feature> soa_features,        ArrayList<soa_Feature> soa_features    ) {
        this.name = name;
        this.soa_exceptions = soa_exceptions;
        this.soa_features = soa_features;
        this.soa_features = soa_features;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<soa_Exception> getSoa_exceptions() {
        return soa_exceptions;
    }

    public void addSoa_exception(Soa_exception soa_exception) {
        this.soa_exceptions.add(soa_exception);
    }
    public List<soa_Feature> getSoa_features() {
        return soa_features;
    }

    public void addSoa_feature(Soa_feature soa_feature) {
        this.soa_features.add(soa_feature);
    }
    public List<soa_Feature> getSoa_features() {
        return soa_features;
    }

    public void addSoa_feature(Soa_feature soa_feature) {
        this.soa_features.add(soa_feature);
    }

}