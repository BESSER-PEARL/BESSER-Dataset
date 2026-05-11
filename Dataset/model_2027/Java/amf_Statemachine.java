





import java.util.List;
import java.util.ArrayList;

public class amf_Statemachine  {

    private String name;





    private amf_Network amf_network;


    public amf_Statemachine(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public amf_Network getAmf_network() {
        return amf_network;
    }

    public void setAmf_network(amf_Network amf_network) {
        this.amf_network = amf_network;
    }

}