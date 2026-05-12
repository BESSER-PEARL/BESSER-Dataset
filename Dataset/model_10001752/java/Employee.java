





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String email;
    private int attendance_count;
    private String emp_id;
    private String DOB;
    private String address;
    private String lname;
    private int phone;
    private String fname;





    private List<Section> sections;


    public Employee(
        String email,        int attendance_count,        String emp_id,        String DOB,        String address,        String lname,        int phone,        String fname    ) {
        this.email = email;
        this.attendance_count = attendance_count;
        this.emp_id = emp_id;
        this.DOB = DOB;
        this.address = address;
        this.lname = lname;
        this.phone = phone;
        this.fname = fname;
        this.sections = new ArrayList<>();
    }

    public Employee(
        String email,        int attendance_count,        String emp_id,        String DOB,        String address,        String lname,        int phone,        String fname        ArrayList<Section> sections    ) {
        this.email = email;
        this.attendance_count = attendance_count;
        this.emp_id = emp_id;
        this.DOB = DOB;
        this.address = address;
        this.lname = lname;
        this.phone = phone;
        this.fname = fname;
        this.sections = sections;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getAttendance_count() {
        return attendance_count;
    }

    public void setAttendance_count(int attendance_count) {
        this.attendance_count = attendance_count;
    }
    public String getEmp_id() {
        return emp_id;
    }

    public void setEmp_id(String emp_id) {
        this.emp_id = emp_id;
    }
    public String getDob() {
        return DOB;
    }

    public void setDob(String DOB) {
        this.DOB = DOB;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getLname() {
        return lname;
    }

    public void setLname(String lname) {
        this.lname = lname;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public String getFname() {
        return fname;
    }

    public void setFname(String fname) {
        this.fname = fname;
    }

    public List<Section> getSections() {
        return sections;
    }

    public void addSection(Section section) {
        this.sections.add(section);
    }

}