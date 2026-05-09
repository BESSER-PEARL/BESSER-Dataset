





import java.util.List;
import java.util.ArrayList;

public class PetriNetModel_Node extends PObject {

    private String name;



    public PetriNetModel_Node(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}