





import java.util.List;
import java.util.ArrayList;

public class resourcePetriNet_Place extends GenericPlace {

    private int capacity;



    public resourcePetriNet_Place(
        int capacity    ) {
        super(
        );
        this.capacity = capacity;
    }


    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }


}