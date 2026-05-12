





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String name;
    private String address;
    private String specialization;
    private String department;
    private int phno;
    private int docid;



    public Doctor(
        String name,        String address,        String specialization,        String department,        int phno,        int docid    ) {
        this.name = name;
        this.address = address;
        this.specialization = specialization;
        this.department = department;
        this.phno = phno;
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
    public String getSpecialization() {
        return specialization;
    }

    public void setSpecialization(String specialization) {
        this.specialization = specialization;
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
    public int getDocid() {
        return docid;
    }

    public void setDocid(int docid) {
        this.docid = docid;
    }


}