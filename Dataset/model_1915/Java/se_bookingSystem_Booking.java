





import java.util.List;
import java.util.ArrayList;

public class se_bookingSystem_Booking extends IBooking {

    private String lastName;
    private String endDate;
    private String startDate;
    private String firstName;
    private int id;





    private List<roomManager_IRoom> roommanager_irooms;




    private List<roomManager_IRoom> roommanager_irooms;


    public se_bookingSystem_Booking(
        String lastName,        String endDate,        String startDate,        String firstName,        int id    ) {
        super(
        );
        this.lastName = lastName;
        this.endDate = endDate;
        this.startDate = startDate;
        this.firstName = firstName;
        this.id = id;
        this.roommanager_irooms = new ArrayList<>();
        this.roommanager_irooms = new ArrayList<>();
    }

    public se_bookingSystem_Booking(
        String lastName,        String endDate,        String startDate,        String firstName,        int id        ArrayList<roomManager_IRoom> roommanager_irooms,        ArrayList<roomManager_IRoom> roommanager_irooms    ) {
        this.lastName = lastName;
        this.endDate = endDate;
        this.startDate = startDate;
        this.firstName = firstName;
        this.id = id;
        this.roommanager_irooms = roommanager_irooms;
        this.roommanager_irooms = roommanager_irooms;
    }

    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getEnddate() {
        return endDate;
    }

    public void setEnddate(String endDate) {
        this.endDate = endDate;
    }
    public String getStartdate() {
        return startDate;
    }

    public void setStartdate(String startDate) {
        this.startDate = startDate;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<roomManager_IRoom> getRoommanager_irooms() {
        return roommanager_irooms;
    }

    public void addRoommanager_iroom(Roommanager_iroom roommanager_iroom) {
        this.roommanager_irooms.add(roommanager_iroom);
    }
    public List<roomManager_IRoom> getRoommanager_irooms() {
        return roommanager_irooms;
    }

    public void addRoommanager_iroom(Roommanager_iroom roommanager_iroom) {
        this.roommanager_irooms.add(roommanager_iroom);
    }

}