





import java.util.List;
import java.util.ArrayList;

public class myffbd_Port  {

    private String id;





    private myffbd_PortType myffbd_porttype;


    public myffbd_Port(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public myffbd_PortType getMyffbd_porttype() {
        return myffbd_porttype;
    }

    public void setMyffbd_porttype(myffbd_PortType myffbd_porttype) {
        this.myffbd_porttype = myffbd_porttype;
    }

}