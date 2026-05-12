





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String address;
    private int phno;
    private int docid;
    private String specialization;
    private String department;
    private String name;



    public Doctor(
        String address,        int phno,        int docid,        String specialization,        String department,        String name    ) {
        this.address = address;
        this.phno = phno;
        this.docid = docid;
        this.specialization = specialization;
        this.department = department;
        this.name = name;
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
    public int getDocid() {
        return docid;
    }

    public void setDocid(int docid) {
        this.docid = docid;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}