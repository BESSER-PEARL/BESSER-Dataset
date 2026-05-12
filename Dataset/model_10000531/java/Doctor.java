





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String name;
    private String address;
    private String department;
    private int phno;
    private String specialization;
    private int docid;



    public Doctor(
        String name,        String address,        String department,        int phno,        String specialization,        int docid    ) {
        this.name = name;
        this.address = address;
        this.department = department;
        this.phno = phno;
        this.specialization = specialization;
        this.docid = docid;
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
    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }
    public int getPhno() {
        return phno;
    }

    public void setPhno(int phno) {
        this.phno = phno;
    }
    public String getSpecialization() {
        return specialization;
    }

    public void setSpecialization(String specialization) {
        this.specialization = specialization;
    }
    public int getDocid() {
        return docid;
    }

    public void setDocid(int docid) {
        this.docid = docid;
    }


}