





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String department;
    private String specialization;
    private String address;
    private int phno;
    private String name;
    private int docid;



    public Doctor(
        String department,        String specialization,        String address,        int phno,        String name,        int docid    ) {
        this.department = department;
        this.specialization = specialization;
        this.address = address;
        this.phno = phno;
        this.name = name;
        this.docid = docid;
    }


    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }
    public String getSpecialization() {
        return specialization;
    }

    public void setSpecialization(String specialization) {
        this.specialization = specialization;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getPhno() {
        return phno;
    }

    public void setPhno(int phno) {
        this.phno = phno;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getDocid() {
        return docid;
    }

    public void setDocid(int docid) {
        this.docid = docid;
    }


}