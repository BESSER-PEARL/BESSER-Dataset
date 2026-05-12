





import java.util.List;
import java.util.ArrayList;

public class receptionist  {

    private String rid;
    private String name;



    public receptionist(
        String rid,        String name    ) {
        this.rid = rid;
        this.name = name;
    }


    public String getRid() {
        return rid;
    }

    public void setRid(String rid) {
        this.rid = rid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}