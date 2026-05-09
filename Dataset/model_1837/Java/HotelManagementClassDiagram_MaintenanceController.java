





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_MaintenanceController  {






    private List<HotelManagementClassDiagram_Room> hotelmanagementclassdiagram_rooms;


    public HotelManagementClassDiagram_MaintenanceController(
    ) {
        this.hotelmanagementclassdiagram_rooms = new ArrayList<>();
    }

    public HotelManagementClassDiagram_MaintenanceController(
        ArrayList<HotelManagementClassDiagram_Room> hotelmanagementclassdiagram_rooms    ) {
        this.hotelmanagementclassdiagram_rooms = hotelmanagementclassdiagram_rooms;
    }


    public List<HotelManagementClassDiagram_Room> getHotelmanagementclassdiagram_rooms() {
        return hotelmanagementclassdiagram_rooms;
    }

    public void addHotelmanagementclassdiagram_room(Hotelmanagementclassdiagram_room hotelmanagementclassdiagram_room) {
        this.hotelmanagementclassdiagram_rooms.add(hotelmanagementclassdiagram_room);
    }

}