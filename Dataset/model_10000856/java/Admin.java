





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String aName;
    private String aId;



    public Admin(
        String aName,        String aId    ) {
        this.aName = aName;
        this.aId = aId;
    }


    public String getAname() {
        return aName;
    }

    public void setAname(String aName) {
        this.aName = aName;
    }
    public String getAid() {
        return aId;
    }

    public void setAid(String aId) {
        this.aId = aId;
    }


}