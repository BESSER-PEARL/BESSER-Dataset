





import java.util.List;
import java.util.ArrayList;

public class noop_Storage  {

    private String type;





    private noop_Member noop_member;


    public noop_Storage(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public noop_Member getNoop_member() {
        return noop_member;
    }

    public void setNoop_member(noop_Member noop_member) {
        this.noop_member = noop_member;
    }

}