





import java.util.List;
import java.util.ArrayList;

public class receptionist  {

    private String name;
    private String rid;



    public receptionist(
        String name,        String rid    ) {
        this.name = name;
        this.rid = rid;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRid() {
        return rid;
    }

    public void setRid(String rid) {
        this.rid = rid;
    }


}