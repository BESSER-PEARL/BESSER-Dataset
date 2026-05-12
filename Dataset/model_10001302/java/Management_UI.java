





import java.util.List;
import java.util.ArrayList;

public class Management_UI  {






    private List<Staff> staffs;


    public Management_UI(
    ) {
        this.staffs = new ArrayList<>();
    }

    public Management_UI(
        ArrayList<Staff> staffs    ) {
        this.staffs = staffs;
    }


    public List<Staff> getStaffs() {
        return staffs;
    }

    public void addStaff(Staff staff) {
        this.staffs.add(staff);
    }

}