





import java.util.List;
import java.util.ArrayList;

public class se_hotelsystem_RoomReservation  {

    private String startDate;
    private String checkInDate;
    private String checkOuDate;
    private String endDate;





    private hotelsystem_RoomType hotelsystem_roomtype;




    private List<hotelsystem_RoomExtra> hotelsystem_roomextras;




    private hotelsystem_Room hotelsystem_room;


    public se_hotelsystem_RoomReservation(
        String startDate,        String checkInDate,        String checkOuDate,        String endDate    ) {
        this.startDate = startDate;
        this.checkInDate = checkInDate;
        this.checkOuDate = checkOuDate;
        this.endDate = endDate;
        this.hotelsystem_roomextras = new ArrayList<>();
    }

    public se_hotelsystem_RoomReservation(
        String startDate,        String checkInDate,        String checkOuDate,        String endDate        ArrayList<hotelsystem_RoomExtra> hotelsystem_roomextras    ) {
        this.startDate = startDate;
        this.checkInDate = checkInDate;
        this.checkOuDate = checkOuDate;
        this.endDate = endDate;
        this.hotelsystem_roomextras = hotelsystem_roomextras;
    }

    public String getStartdate() {
        return startDate;
    }

    public void setStartdate(String startDate) {
        this.startDate = startDate;
    }
    public String getCheckindate() {
        return checkInDate;
    }

    public void setCheckindate(String checkInDate) {
        this.checkInDate = checkInDate;
    }
    public String getCheckoudate() {
        return checkOuDate;
    }

    public void setCheckoudate(String checkOuDate) {
        this.checkOuDate = checkOuDate;
    }
    public String getEnddate() {
        return endDate;
    }

    public void setEnddate(String endDate) {
        this.endDate = endDate;
    }

    public hotelsystem_RoomType getHotelsystem_roomtype() {
        return hotelsystem_roomtype;
    }

    public void setHotelsystem_roomtype(hotelsystem_RoomType hotelsystem_roomtype) {
        this.hotelsystem_roomtype = hotelsystem_roomtype;
    }
    public List<hotelsystem_RoomExtra> getHotelsystem_roomextras() {
        return hotelsystem_roomextras;
    }

    public void addHotelsystem_roomextra(Hotelsystem_roomextra hotelsystem_roomextra) {
        this.hotelsystem_roomextras.add(hotelsystem_roomextra);
    }
    public hotelsystem_Room getHotelsystem_room() {
        return hotelsystem_room;
    }

    public void setHotelsystem_room(hotelsystem_Room hotelsystem_room) {
        this.hotelsystem_room = hotelsystem_room;
    }

}