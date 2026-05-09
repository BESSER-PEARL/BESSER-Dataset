





import java.util.List;
import java.util.ArrayList;

public class Classes_RoomType  {

    private String roomTypeName;
    private String numberOfGuests;
    private String features;
    private String description;
    private String price;





    private List<Classes_Room> classes_rooms;




    private Classes_Room classes_room;


    public Classes_RoomType(
        String roomTypeName,        String numberOfGuests,        String features,        String description,        String price    ) {
        this.roomTypeName = roomTypeName;
        this.numberOfGuests = numberOfGuests;
        this.features = features;
        this.description = description;
        this.price = price;
        this.classes_rooms = new ArrayList<>();
    }

    public Classes_RoomType(
        String roomTypeName,        String numberOfGuests,        String features,        String description,        String price        ArrayList<Classes_Room> classes_rooms    ) {
        this.roomTypeName = roomTypeName;
        this.numberOfGuests = numberOfGuests;
        this.features = features;
        this.description = description;
        this.price = price;
        this.classes_rooms = classes_rooms;
    }

    public String getRoomtypename() {
        return roomTypeName;
    }

    public void setRoomtypename(String roomTypeName) {
        this.roomTypeName = roomTypeName;
    }
    public String getNumberofguests() {
        return numberOfGuests;
    }

    public void setNumberofguests(String numberOfGuests) {
        this.numberOfGuests = numberOfGuests;
    }
    public String getFeatures() {
        return features;
    }

    public void setFeatures(String features) {
        this.features = features;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }

    public List<Classes_Room> getClasses_rooms() {
        return classes_rooms;
    }

    public void addClasses_room(Classes_room classes_room) {
        this.classes_rooms.add(classes_room);
    }
    public Classes_Room getClasses_room() {
        return classes_room;
    }

    public void setClasses_room(Classes_Room classes_room) {
        this.classes_room = classes_room;
    }

}