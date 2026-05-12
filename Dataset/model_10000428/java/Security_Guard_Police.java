





import java.util.List;
import java.util.ArrayList;

public class Security_Guard_Police  {

    private int sgpID;





    private Alert alert;


    public Security_Guard_Police(
        int sgpID    ) {
        this.sgpID = sgpID;
    }


    public int getSgpid() {
        return sgpID;
    }

    public void setSgpid(int sgpID) {
        this.sgpID = sgpID;
    }

    public Alert getAlert() {
        return alert;
    }

    public void setAlert(Alert alert) {
        this.alert = alert;
    }

}