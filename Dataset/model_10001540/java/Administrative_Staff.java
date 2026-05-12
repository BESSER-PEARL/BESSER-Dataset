





import java.util.List;
import java.util.ArrayList;

public class Administrative_Staff  {

    private String ReceptionistName;
    private String FrontDeskStaffName;



    public Administrative_Staff(
        String ReceptionistName,        String FrontDeskStaffName    ) {
        this.ReceptionistName = ReceptionistName;
        this.FrontDeskStaffName = FrontDeskStaffName;
    }


    public String getReceptionistname() {
        return ReceptionistName;
    }

    public void setReceptionistname(String ReceptionistName) {
        this.ReceptionistName = ReceptionistName;
    }
    public String getFrontdeskstaffname() {
        return FrontDeskStaffName;
    }

    public void setFrontdeskstaffname(String FrontDeskStaffName) {
        this.FrontDeskStaffName = FrontDeskStaffName;
    }


}