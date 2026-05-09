





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_EmployeeType  {

    private int acessLevel;
    private String type;





    private HotelManagementClassDiagram_Employee hotelmanagementclassdiagram_employee;


    public HotelManagementClassDiagram_EmployeeType(
        int acessLevel,        String type    ) {
        this.acessLevel = acessLevel;
        this.type = type;
    }


    public int getAcesslevel() {
        return acessLevel;
    }

    public void setAcesslevel(int acessLevel) {
        this.acessLevel = acessLevel;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public HotelManagementClassDiagram_Employee getHotelmanagementclassdiagram_employee() {
        return hotelmanagementclassdiagram_employee;
    }

    public void setHotelmanagementclassdiagram_employee(HotelManagementClassDiagram_Employee hotelmanagementclassdiagram_employee) {
        this.hotelmanagementclassdiagram_employee = hotelmanagementclassdiagram_employee;
    }

}