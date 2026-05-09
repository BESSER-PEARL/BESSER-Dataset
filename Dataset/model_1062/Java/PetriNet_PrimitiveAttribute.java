





import java.util.List;
import java.util.ArrayList;

public class PetriNet_PrimitiveAttribute  {

    private String primType;
    private String name;





    private PetriNet_Type petrinet_type;


    public PetriNet_PrimitiveAttribute(
        String primType,        String name    ) {
        this.primType = primType;
        this.name = name;
    }


    public String getPrimtype() {
        return primType;
    }

    public void setPrimtype(String primType) {
        this.primType = primType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PetriNet_Type getPetrinet_type() {
        return petrinet_type;
    }

    public void setPetrinet_type(PetriNet_Type petrinet_type) {
        this.petrinet_type = petrinet_type;
    }

}