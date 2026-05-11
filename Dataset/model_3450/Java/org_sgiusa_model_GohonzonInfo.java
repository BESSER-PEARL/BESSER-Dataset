





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_GohonzonInfo  {

    private String returnDate;
    private String lastUpdate;
    private String receiveDate;
    private String id;
    private String gohonzonType;
    private String returned;



    public org_sgiusa_model_GohonzonInfo(
        String returnDate,        String lastUpdate,        String receiveDate,        String id,        String gohonzonType,        String returned    ) {
        this.returnDate = returnDate;
        this.lastUpdate = lastUpdate;
        this.receiveDate = receiveDate;
        this.id = id;
        this.gohonzonType = gohonzonType;
        this.returned = returned;
    }


    public String getReturndate() {
        return returnDate;
    }

    public void setReturndate(String returnDate) {
        this.returnDate = returnDate;
    }
    public String getLastupdate() {
        return lastUpdate;
    }

    public void setLastupdate(String lastUpdate) {
        this.lastUpdate = lastUpdate;
    }
    public String getReceivedate() {
        return receiveDate;
    }

    public void setReceivedate(String receiveDate) {
        this.receiveDate = receiveDate;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getGohonzontype() {
        return gohonzonType;
    }

    public void setGohonzontype(String gohonzonType) {
        this.gohonzonType = gohonzonType;
    }
    public String getReturned() {
        return returned;
    }

    public void setReturned(String returned) {
        this.returned = returned;
    }


}