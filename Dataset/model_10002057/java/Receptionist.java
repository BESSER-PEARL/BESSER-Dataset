





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {

    private int Employee_ID;
    private String Name;



    public Receptionist(
        int Employee_ID,        String Name    ) {
        this.Employee_ID = Employee_ID;
        this.Name = Name;
    }


    public int getEmployee_id() {
        return Employee_ID;
    }

    public void setEmployee_id(int Employee_ID) {
        this.Employee_ID = Employee_ID;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}