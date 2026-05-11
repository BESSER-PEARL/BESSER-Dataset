





import java.util.List;
import java.util.ArrayList;

public class amf_Channel  {

    private String Type;
    private String name;





    private amf_Network amf_network;


    public amf_Channel(
        String Type,        String name    ) {
        this.Type = Type;
        this.name = name;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
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