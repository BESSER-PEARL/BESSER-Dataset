





import java.util.List;
import java.util.ArrayList;

public class Department  {






    private List<Staff> staffs;




    private Hospital hospital;


    public Department(
    ) {
        this.staffs = new ArrayList<>();
    }

    public Department(
        ArrayList<Staff> staffs    ) {
        this.staffs = staffs;
    }


    public List<Staff> getStaffs() {
        return staffs;
    }

    public void addStaff(Staff staff) {
        this.staffs.add(staff);
    }
    public Hospital getHospital() {
        return hospital;
    }

    public void setHospital(Hospital hospital) {
        this.hospital = hospital;
    }

}