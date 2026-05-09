





import java.util.List;
import java.util.ArrayList;

public class newClasses_Booking extends ServiceProvider, RoomProvider, Validator, Biller, CustomerProvides, Booker {

    private String conformationNum;
    private String services;
    private String cost;
    private String roomType;
    private String checkOutDate;
    private String isPaid;
    private String checkInDate;





    private newClasses_Customer newclasses_customer;


    public newClasses_Booking(
        String conformationNum,        String services,        String cost,        String roomType,        String checkOutDate,        String isPaid,        String checkInDate    ) {
        super(
        );
        this.conformationNum = conformationNum;
        this.services = services;
        this.cost = cost;
        this.roomType = roomType;
        this.checkOutDate = checkOutDate;
        this.isPaid = isPaid;
        this.checkInDate = checkInDate;
    }


    public String getConformationnum() {
        return conformationNum;
    }

    public void setConformationnum(String conformationNum) {
        this.conformationNum = conformationNum;
    }
    public String getServices() {
        return services;
    }

    public void setServices(String services) {
        this.services = services;
    }
    public String getCost() {
        return cost;
    }

    public void setCost(String cost) {
        this.cost = cost;
    }
    public String getRoomtype() {
        return roomType;
    }

    public void setRoomtype(String roomType) {
        this.roomType = roomType;
    }
    public String getCheckoutdate() {
        return checkOutDate;
    }

    public void setCheckoutdate(String checkOutDate) {
        this.checkOutDate = checkOutDate;
    }
    public String getIspaid() {
        return isPaid;
    }

    public void setIspaid(String isPaid) {
        this.isPaid = isPaid;
    }
    public String getCheckindate() {
        return checkInDate;
    }

    public void setCheckindate(String checkInDate) {
        this.checkInDate = checkInDate;
    }

    public newClasses_Customer getNewclasses_customer() {
        return newclasses_customer;
    }

    public void setNewclasses_customer(newClasses_Customer newclasses_customer) {
        this.newclasses_customer = newclasses_customer;
    }

}