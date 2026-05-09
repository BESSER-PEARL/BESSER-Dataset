





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Place extends Element {

    private String name;



    public PetriNet_Place(
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