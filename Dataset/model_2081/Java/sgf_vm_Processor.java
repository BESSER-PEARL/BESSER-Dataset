





import java.util.List;
import java.util.ArrayList;

public class sgf_vm_Processor  {

    private String ID;
    private String IP;



    public sgf_vm_Processor(
        String ID,        String IP    ) {
        this.ID = ID;
        this.IP = IP;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getIp() {
        return IP;
    }

    public void setIp(String IP) {
        this.IP = IP;
    }


}