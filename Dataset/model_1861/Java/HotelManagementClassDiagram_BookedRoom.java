





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_BookedRoom extends Room {






    private List<HotelManagementClassDiagram_Addon> hotelmanagementclassdiagram_addons;


    public HotelManagementClassDiagram_BookedRoom(
    ) {
        super(
        );
        this.hotelmanagementclassdiagram_addons = new ArrayList<>();
    }

    public HotelManagementClassDiagram_BookedRoom(
        ArrayList<HotelManagementClassDiagram_Addon> hotelmanagementclassdiagram_addons    ) {
        this.hotelmanagementclassdiagram_addons = hotelmanagementclassdiagram_addons;
    }


    public List<HotelManagementClassDiagram_Addon> getHotelmanagementclassdiagram_addons() {
        return hotelmanagementclassdiagram_addons;
    }

    public void addHotelmanagementclassdiagram_addon(Hotelmanagementclassdiagram_addon hotelmanagementclassdiagram_addon) {
        this.hotelmanagementclassdiagram_addons.add(hotelmanagementclassdiagram_addon);
    }

}