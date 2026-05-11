





import java.util.List;
import java.util.ArrayList;

public class ra_Programme  {

    private String mCode;
    private String name;





    private ra_Department ra_department;


    public ra_Programme(
        String mCode,        String name    ) {
        this.mCode = mCode;
        this.name = name;
    }


    public String getMcode() {
        return mCode;
    }

    public void setMcode(String mCode) {
        this.mCode = mCode;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ra_Department getRa_department() {
        return ra_department;
    }

    public void setRa_department(ra_Department ra_department) {
        this.ra_department = ra_department;
    }

}