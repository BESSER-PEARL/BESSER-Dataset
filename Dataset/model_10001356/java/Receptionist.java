





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {

    private String Rid;
    private String Rname;



    public Receptionist(
        String Rid,        String Rname    ) {
        this.Rid = Rid;
        this.Rname = Rname;
    }


    public String getRid() {
        return Rid;
    }

    public void setRid(String Rid) {
        this.Rid = Rid;
    }
    public String getRname() {
        return Rname;
    }

    public void setRname(String Rname) {
        this.Rname = Rname;
    }


}