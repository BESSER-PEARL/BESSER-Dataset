





import java.util.List;
import java.util.ArrayList;

public class RoomService  {

    private String itemsCollection;
    private String idiomas;
    private String niveles;
    private String roomsCollection;





    private Room_Interface room_interface;


    public RoomService(
        String itemsCollection,        String idiomas,        String niveles,        String roomsCollection    ) {
        this.itemsCollection = itemsCollection;
        this.idiomas = idiomas;
        this.niveles = niveles;
        this.roomsCollection = roomsCollection;
    }


    public String getItemscollection() {
        return itemsCollection;
    }

    public void setItemscollection(String itemsCollection) {
        this.itemsCollection = itemsCollection;
    }
    public String getIdiomas() {
        return idiomas;
    }

    public void setIdiomas(String idiomas) {
        this.idiomas = idiomas;
    }
    public String getNiveles() {
        return niveles;
    }

    public void setNiveles(String niveles) {
        this.niveles = niveles;
    }
    public String getRoomscollection() {
        return roomsCollection;
    }

    public void setRoomscollection(String roomsCollection) {
        this.roomsCollection = roomsCollection;
    }

    public Room_Interface getRoom_interface() {
        return room_interface;
    }

    public void setRoom_interface(Room_Interface room_interface) {
        this.room_interface = room_interface;
    }

}