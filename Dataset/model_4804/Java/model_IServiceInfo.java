





import java.util.List;
import java.util.ArrayList;

public class model_IServiceInfo  {

    private String ecfServiceInfo;
    private String ecfLocation;
    private String ecfName;
    private int ecfPriority;
    private int ecfWeight;



    public model_IServiceInfo(
        String ecfServiceInfo,        String ecfLocation,        String ecfName,        int ecfPriority,        int ecfWeight    ) {
        this.ecfServiceInfo = ecfServiceInfo;
        this.ecfLocation = ecfLocation;
        this.ecfName = ecfName;
        this.ecfPriority = ecfPriority;
        this.ecfWeight = ecfWeight;
    }


    public String getEcfserviceinfo() {
        return ecfServiceInfo;
    }

    public void setEcfserviceinfo(String ecfServiceInfo) {
        this.ecfServiceInfo = ecfServiceInfo;
    }
    public String getEcflocation() {
        return ecfLocation;
    }

    public void setEcflocation(String ecfLocation) {
        this.ecfLocation = ecfLocation;
    }
    public String getEcfname() {
        return ecfName;
    }

    public void setEcfname(String ecfName) {
        this.ecfName = ecfName;
    }
    public int getEcfpriority() {
        return ecfPriority;
    }

    public void setEcfpriority(int ecfPriority) {
        this.ecfPriority = ecfPriority;
    }
    public int getEcfweight() {
        return ecfWeight;
    }

    public void setEcfweight(int ecfWeight) {
        this.ecfWeight = ecfWeight;
    }


}