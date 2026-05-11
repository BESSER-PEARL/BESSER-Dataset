





import java.util.List;
import java.util.ArrayList;

public class dsl_ServiceMetaData extends Metadata {

    private String serviceID;





    private dsl_RunTimeModel dsl_runtimemodel;


    public dsl_ServiceMetaData(
        String serviceID    ) {
        super(
        );
        this.serviceID = serviceID;
    }


    public String getServiceid() {
        return serviceID;
    }

    public void setServiceid(String serviceID) {
        this.serviceID = serviceID;
    }

    public dsl_RunTimeModel getDsl_runtimemodel() {
        return dsl_runtimemodel;
    }

    public void setDsl_runtimemodel(dsl_RunTimeModel dsl_runtimemodel) {
        this.dsl_runtimemodel = dsl_runtimemodel;
    }

}