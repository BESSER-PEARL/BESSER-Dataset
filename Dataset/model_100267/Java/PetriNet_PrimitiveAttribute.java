





import java.util.List;
import java.util.ArrayList;

public class PetriNet_PrimitiveAttribute  {

    private String name;
    private String primType;





    private PetriNet_Type petrinet_type;


    public PetriNet_PrimitiveAttribute(
        String name,        String primType    ) {
        this.name = name;
        this.primType = primType;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPrimtype() {
        return primType;
    }

    public void setPrimtype(String primType) {
        this.primType = primType;
    }

    public PetriNet_Type getPetrinet_type() {
        return petrinet_type;
    }

    public void setPetrinet_type(PetriNet_Type petrinet_type) {
        this.petrinet_type = petrinet_type;
    }

}