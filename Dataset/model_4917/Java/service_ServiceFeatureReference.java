





import java.util.List;
import java.util.ArrayList;

public class service_ServiceFeatureReference extends Variable {

    private String name;





    private service_Feature service_feature;


    public service_ServiceFeatureReference(
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

    public service_Feature getService_feature() {
        return service_feature;
    }

    public void setService_feature(service_Feature service_feature) {
        this.service_feature = service_feature;
    }

}