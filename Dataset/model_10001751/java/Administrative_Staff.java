





import java.util.List;
import java.util.ArrayList;

public class Administrative_Staff  {

    private String FrontDeskStaffName;
    private String ReceptionistName;



    public Administrative_Staff(
        String FrontDeskStaffName,        String ReceptionistName    ) {
        this.FrontDeskStaffName = FrontDeskStaffName;
        this.ReceptionistName = ReceptionistName;
    }


    public String getFrontdeskstaffname() {
        return FrontDeskStaffName;
    }

    public void setFrontdeskstaffname(String FrontDeskStaffName) {
        this.FrontDeskStaffName = FrontDeskStaffName;
    }
    public String getReceptionistname() {
        return ReceptionistName;
    }

    public void setReceptionistname(String ReceptionistName) {
        this.ReceptionistName = ReceptionistName;
    }


}