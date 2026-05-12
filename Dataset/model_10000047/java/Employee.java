





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String lname;
    private int phone;
    private String emp_id;
    private int attendance_count;
    private String email;
    private String fname;
    private String DOB;
    private String address;





    private List<Section> sections;


    public Employee(
        String lname,        int phone,        String emp_id,        int attendance_count,        String email,        String fname,        String DOB,        String address    ) {
        this.lname = lname;
        this.phone = phone;
        this.emp_id = emp_id;
        this.attendance_count = attendance_count;
        this.email = email;
        this.fname = fname;
        this.DOB = DOB;
        this.address = address;
        this.sections = new ArrayList<>();
    }

    public Employee(
        String lname,        int phone,        String emp_id,        int attendance_count,        String email,        String fname,        String DOB,        String address        ArrayList<Section> sections    ) {
        this.lname = lname;
        this.phone = phone;
        this.emp_id = emp_id;
        this.attendance_count = attendance_count;
        this.email = email;
        this.fname = fname;
        this.DOB = DOB;
        this.address = address;
        this.sections = sections;
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
    public String getEmp_id() {
        return emp_id;
    }

    public void setEmp_id(String emp_id) {
        this.emp_id = emp_id;
    }
    public int getAttendance_count() {
        return attendance_count;
    }

    public void setAttendance_count(int attendance_count) {
        this.attendance_count = attendance_count;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getFname() {
        return fname;
    }

    public void setFname(String fname) {
        this.fname = fname;
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

    public List<Section> getSections() {
        return sections;
    }

    public void addSection(Section section) {
        this.sections.add(section);
    }

}