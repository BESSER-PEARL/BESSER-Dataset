





import java.util.List;
import java.util.ArrayList;

public class softwaretraces_Feature extends MyNode {

    private String name;





    private softwaretraces_Model softwaretraces_model;




    private softwaretraces_Feature softwaretraces_feature;


    public softwaretraces_Feature(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public softwaretraces_Model getSoftwaretraces_model() {
        return softwaretraces_model;
    }

    public void setSoftwaretraces_model(softwaretraces_Model softwaretraces_model) {
        this.softwaretraces_model = softwaretraces_model;
    }
    public softwaretraces_Feature getSoftwaretraces_feature() {
        return softwaretraces_feature;
    }

    public void setSoftwaretraces_feature(softwaretraces_Feature softwaretraces_feature) {
        this.softwaretraces_feature = softwaretraces_feature;
    }

}