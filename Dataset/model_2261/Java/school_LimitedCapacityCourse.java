





import java.util.List;
import java.util.ArrayList;

public class school_LimitedCapacityCourse extends Course {

    private int capacity;



    public school_LimitedCapacityCourse(
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