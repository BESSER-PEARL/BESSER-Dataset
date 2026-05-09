





import java.util.List;
import java.util.ArrayList;

public class domain_Orders  {

    private String uid;





    private domain_DataControl domain_datacontrol;


    public domain_Orders(
        String uid    ) {
        this.uid = uid;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_DataControl getDomain_datacontrol() {
        return domain_datacontrol;
    }

    public void setDomain_datacontrol(domain_DataControl domain_datacontrol) {
        this.domain_datacontrol = domain_datacontrol;
    }

}