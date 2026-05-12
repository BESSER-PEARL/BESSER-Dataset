





import java.util.List;
import java.util.ArrayList;

public class Department  {






    private Hospital hospital;




    private List<Staff> staffs;


    public Department(
    ) {
        this.staffs = new ArrayList<>();
    }

    public Department(
        ArrayList<Staff> staffs    ) {
        this.staffs = staffs;
    }


    public Hospital getHospital() {
        return hospital;
    }

    public void setHospital(Hospital hospital) {
        this.hospital = hospital;
    }
    public List<Staff> getStaffs() {
        return staffs;
    }

    public void addStaff(Staff staff) {
        this.staffs.add(staff);
    }

}