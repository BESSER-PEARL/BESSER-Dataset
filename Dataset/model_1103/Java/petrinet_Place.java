





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place extends Node {

    private int capacity;



    public petrinet_Place(
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