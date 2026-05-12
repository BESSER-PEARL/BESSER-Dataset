





import java.util.List;
import java.util.ArrayList;

public class petriNet_Place extends GenericPlace {

    private int capacity;



    public petriNet_Place(
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