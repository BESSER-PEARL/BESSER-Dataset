





import java.util.List;
import java.util.ArrayList;

public class Nurse  {

    private String name;
    private int id;





    private Staff staff;


    public Nurse(
        String name,        int id    ) {
        this.name = name;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Staff getStaff() {
        return staff;
    }

    public void setStaff(Staff staff) {
        this.staff = staff;
    }

}