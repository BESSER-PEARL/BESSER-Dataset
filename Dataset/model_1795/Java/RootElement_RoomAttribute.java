





import java.util.List;
import java.util.ArrayList;

public class RootElement_RoomAttribute  {

    private String name;
    private String description;
    private String id;





    private RootElement_RoomType rootelement_roomtype;


    public RootElement_RoomAttribute(
        String name,        String description,        String id    ) {
        this.name = name;
        this.description = description;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public RootElement_RoomType getRootelement_roomtype() {
        return rootelement_roomtype;
    }

    public void setRootelement_roomtype(RootElement_RoomType rootelement_roomtype) {
        this.rootelement_roomtype = rootelement_roomtype;
    }

}