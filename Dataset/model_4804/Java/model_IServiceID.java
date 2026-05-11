





import java.util.List;
import java.util.ArrayList;

public class model_IServiceID  {

    private String ecfServiceName;
    private String ecfServiceID;





    private model_IServiceInfo model_iserviceinfo;


    public model_IServiceID(
        String ecfServiceName,        String ecfServiceID    ) {
        this.ecfServiceName = ecfServiceName;
        this.ecfServiceID = ecfServiceID;
    }


    public String getEcfservicename() {
        return ecfServiceName;
    }

    public void setEcfservicename(String ecfServiceName) {
        this.ecfServiceName = ecfServiceName;
    }
    public String getEcfserviceid() {
        return ecfServiceID;
    }

    public void setEcfserviceid(String ecfServiceID) {
        this.ecfServiceID = ecfServiceID;
    }

    public model_IServiceInfo getModel_iserviceinfo() {
        return model_iserviceinfo;
    }

    public void setModel_iserviceinfo(model_IServiceInfo model_iserviceinfo) {
        this.model_iserviceinfo = model_iserviceinfo;
    }

}