





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String department;
    private String specialization;
    private int phno;
    private String address;
    private int docid;
    private String name;



    public Doctor(
        String department,        String specialization,        int phno,        String address,        int docid,        String name    ) {
        this.department = department;
        this.specialization = specialization;
        this.phno = phno;
        this.address = address;
        this.docid = docid;
        this.name = name;
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
    public int getPhno() {
        return phno;
    }

    public void setPhno(int phno) {
        this.phno = phno;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getDocid() {
        return docid;
    }

    public void setDocid(int docid) {
        this.docid = docid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}