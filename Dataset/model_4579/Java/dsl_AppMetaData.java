





import java.util.List;
import java.util.ArrayList;

public class dsl_AppMetaData extends Metadata {

    private String appID;





    private dsl_RunTimeModel dsl_runtimemodel;


    public dsl_AppMetaData(
        String appID    ) {
        super(
        );
        this.appID = appID;
    }


    public String getAppid() {
        return appID;
    }

    public void setAppid(String appID) {
        this.appID = appID;
    }

    public dsl_RunTimeModel getDsl_runtimemodel() {
        return dsl_runtimemodel;
    }

    public void setDsl_runtimemodel(dsl_RunTimeModel dsl_runtimemodel) {
        this.dsl_runtimemodel = dsl_runtimemodel;
    }

}