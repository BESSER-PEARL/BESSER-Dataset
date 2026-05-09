





import java.util.List;
import java.util.ArrayList;

public class Classes_Services_RoomServiceMenu  {

    private String name;
    private String items;



    public Classes_Services_RoomServiceMenu(
        String name,        String items    ) {
        this.name = name;
        this.items = items;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getItems() {
        return items;
    }

    public void setItems(String items) {
        this.items = items;
    }


}