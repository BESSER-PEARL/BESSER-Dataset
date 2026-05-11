





import java.util.List;
import java.util.ArrayList;

public class fopramodel_Person  {

    private String forename;
    private String lastname;





    private fopramodel_FoPraManagementSystem fopramodel_fopramanagementsystem;


    public fopramodel_Person(
        String forename,        String lastname    ) {
        this.forename = forename;
        this.lastname = lastname;
    }


    public String getForename() {
        return forename;
    }

    public void setForename(String forename) {
        this.forename = forename;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public fopramodel_FoPraManagementSystem getFopramodel_fopramanagementsystem() {
        return fopramodel_fopramanagementsystem;
    }

    public void setFopramodel_fopramanagementsystem(fopramodel_FoPraManagementSystem fopramodel_fopramanagementsystem) {
        this.fopramodel_fopramanagementsystem = fopramodel_fopramanagementsystem;
    }

}