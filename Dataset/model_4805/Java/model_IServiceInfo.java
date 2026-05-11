





import java.util.List;
import java.util.ArrayList;

public class model_IServiceInfo  {

    private int ecfWeight;
    private String ecfLocation;
    private String ecfServiceInfo;
    private String ecfName;
    private int ecfPriority;



    public model_IServiceInfo(
        int ecfWeight,        String ecfLocation,        String ecfServiceInfo,        String ecfName,        int ecfPriority    ) {
        this.ecfWeight = ecfWeight;
        this.ecfLocation = ecfLocation;
        this.ecfServiceInfo = ecfServiceInfo;
        this.ecfName = ecfName;
        this.ecfPriority = ecfPriority;
    }


    public int getEcfweight() {
        return ecfWeight;
    }

    public void setEcfweight(int ecfWeight) {
        this.ecfWeight = ecfWeight;
    }
    public String getEcflocation() {
        return ecfLocation;
    }

    public void setEcflocation(String ecfLocation) {
        this.ecfLocation = ecfLocation;
    }
    public String getEcfserviceinfo() {
        return ecfServiceInfo;
    }

    public void setEcfserviceinfo(String ecfServiceInfo) {
        this.ecfServiceInfo = ecfServiceInfo;
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


}