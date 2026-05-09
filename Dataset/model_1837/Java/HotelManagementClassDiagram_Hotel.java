





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Hotel  {

    private String name;
    private String address;
    private float rank;





    private HotelManagementClassDiagram_BookingController hotelmanagementclassdiagram_bookingcontroller;




    private HotelManagementClassDiagram_MaintenanceController hotelmanagementclassdiagram_maintenancecontroller;




    private HotelManagementClassDiagram_Employee hotelmanagementclassdiagram_employee;




    private HotelManagementClassDiagram_ManagementController hotelmanagementclassdiagram_managementcontroller;


    public HotelManagementClassDiagram_Hotel(
        String name,        String address,        float rank    ) {
        this.name = name;
        this.address = address;
        this.rank = rank;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public float getRank() {
        return rank;
    }

    public void setRank(float rank) {
        this.rank = rank;
    }

    public HotelManagementClassDiagram_BookingController getHotelmanagementclassdiagram_bookingcontroller() {
        return hotelmanagementclassdiagram_bookingcontroller;
    }

    public void setHotelmanagementclassdiagram_bookingcontroller(HotelManagementClassDiagram_BookingController hotelmanagementclassdiagram_bookingcontroller) {
        this.hotelmanagementclassdiagram_bookingcontroller = hotelmanagementclassdiagram_bookingcontroller;
    }
    public HotelManagementClassDiagram_MaintenanceController getHotelmanagementclassdiagram_maintenancecontroller() {
        return hotelmanagementclassdiagram_maintenancecontroller;
    }

    public void setHotelmanagementclassdiagram_maintenancecontroller(HotelManagementClassDiagram_MaintenanceController hotelmanagementclassdiagram_maintenancecontroller) {
        this.hotelmanagementclassdiagram_maintenancecontroller = hotelmanagementclassdiagram_maintenancecontroller;
    }
    public HotelManagementClassDiagram_Employee getHotelmanagementclassdiagram_employee() {
        return hotelmanagementclassdiagram_employee;
    }

    public void setHotelmanagementclassdiagram_employee(HotelManagementClassDiagram_Employee hotelmanagementclassdiagram_employee) {
        this.hotelmanagementclassdiagram_employee = hotelmanagementclassdiagram_employee;
    }
    public HotelManagementClassDiagram_ManagementController getHotelmanagementclassdiagram_managementcontroller() {
        return hotelmanagementclassdiagram_managementcontroller;
    }

    public void setHotelmanagementclassdiagram_managementcontroller(HotelManagementClassDiagram_ManagementController hotelmanagementclassdiagram_managementcontroller) {
        this.hotelmanagementclassdiagram_managementcontroller = hotelmanagementclassdiagram_managementcontroller;
    }

}