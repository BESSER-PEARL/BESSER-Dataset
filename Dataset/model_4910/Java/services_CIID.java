





import java.util.List;
import java.util.ArrayList;

public class services_CIID extends Base {

    private String commonCIID;
    private String localCIID;



    public services_CIID(
        String commonCIID,        String localCIID    ) {
        super(
        );
        this.commonCIID = commonCIID;
        this.localCIID = localCIID;
    }


    public String getCommonciid() {
        return commonCIID;
    }

    public void setCommonciid(String commonCIID) {
        this.commonCIID = commonCIID;
    }
    public String getLocalciid() {
        return localCIID;
    }

    public void setLocalciid(String localCIID) {
        this.localCIID = localCIID;
    }


}