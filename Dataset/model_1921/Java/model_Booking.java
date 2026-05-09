




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_Booking  {

    private String wishes;
    private int id;
    private LocalDate toDate;
    private LocalDate fromDate;
    private String checkedIn;
    private String roomTypes;
    private String promotion;





    private model_Receipt model_receipt;




    private model_Customer model_customer;




    private List<model_Room> model_rooms;


    public model_Booking(
        String wishes,        int id,        LocalDate toDate,        LocalDate fromDate,        String checkedIn,        String roomTypes,        String promotion    ) {
        this.wishes = wishes;
        this.id = id;
        this.toDate = toDate;
        this.fromDate = fromDate;
        this.checkedIn = checkedIn;
        this.roomTypes = roomTypes;
        this.promotion = promotion;
        this.model_rooms = new ArrayList<>();
    }

    public model_Booking(
        String wishes,        int id,        LocalDate toDate,        LocalDate fromDate,        String checkedIn,        String roomTypes,        String promotion        ArrayList<model_Room> model_rooms    ) {
        this.wishes = wishes;
        this.id = id;
        this.toDate = toDate;
        this.fromDate = fromDate;
        this.checkedIn = checkedIn;
        this.roomTypes = roomTypes;
        this.promotion = promotion;
        this.model_rooms = model_rooms;
    }

    public String getWishes() {
        return wishes;
    }

    public void setWishes(String wishes) {
        this.wishes = wishes;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public LocalDate getTodate() {
        return toDate;
    }

    public void setTodate(LocalDate toDate) {
        this.toDate = toDate;
    }
    public LocalDate getFromdate() {
        return fromDate;
    }

    public void setFromdate(LocalDate fromDate) {
        this.fromDate = fromDate;
    }
    public String getCheckedin() {
        return checkedIn;
    }

    public void setCheckedin(String checkedIn) {
        this.checkedIn = checkedIn;
    }
    public String getRoomtypes() {
        return roomTypes;
    }

    public void setRoomtypes(String roomTypes) {
        this.roomTypes = roomTypes;
    }
    public String getPromotion() {
        return promotion;
    }

    public void setPromotion(String promotion) {
        this.promotion = promotion;
    }

    public model_Receipt getModel_receipt() {
        return model_receipt;
    }

    public void setModel_receipt(model_Receipt model_receipt) {
        this.model_receipt = model_receipt;
    }
    public model_Customer getModel_customer() {
        return model_customer;
    }

    public void setModel_customer(model_Customer model_customer) {
        this.model_customer = model_customer;
    }
    public List<model_Room> getModel_rooms() {
        return model_rooms;
    }

    public void addModel_room(Model_room model_room) {
        this.model_rooms.add(model_room);
    }

}