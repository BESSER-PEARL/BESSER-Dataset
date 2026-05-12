





import java.util.List;
import java.util.ArrayList;

public class StaffUI  {






    private List<Staff> staffs;


    public StaffUI(
    ) {
        this.staffs = new ArrayList<>();
    }

    public StaffUI(
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