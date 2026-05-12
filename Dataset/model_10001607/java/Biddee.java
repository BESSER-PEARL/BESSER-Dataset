





import java.util.List;
import java.util.ArrayList;

public class Biddee  {

    private String statusBiddee;





    private Admin admin;


    public Biddee(
        String statusBiddee    ) {
        this.statusBiddee = statusBiddee;
    }


    public String getStatusbiddee() {
        return statusBiddee;
    }

    public void setStatusbiddee(String statusBiddee) {
        this.statusBiddee = statusBiddee;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}