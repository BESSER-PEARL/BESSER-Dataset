





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_Container  {

    private String ID;
    private String IP_address;



    public ioT_metamodel_Container(
        String ID,        String IP_address    ) {
        this.ID = ID;
        this.IP_address = IP_address;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getIp_address() {
        return IP_address;
    }

    public void setIp_address(String IP_address) {
        this.IP_address = IP_address;
    }


}