





import java.util.List;
import java.util.ArrayList;

public class Classes_Bookables_ConferenceRoom extends Room {

    private String capacity;
    private String category;



    public Classes_Bookables_ConferenceRoom(
        String capacity,        String category    ) {
        super(
        );
        this.capacity = capacity;
        this.category = category;
    }


    public String getCapacity() {
        return capacity;
    }

    public void setCapacity(String capacity) {
        this.capacity = capacity;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }


}