





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String address;
    private String name;
    private String specialization;
    private int docid;
    private int phno;
    private String department;



    public Doctor(
        String address,        String name,        String specialization,        int docid,        int phno,        String department    ) {
        this.address = address;
        this.name = name;
        this.specialization = specialization;
        this.docid = docid;
        this.phno = phno;
        this.department = department;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public int getPhno() {
        return phno;
    }

    public void setPhno(int phno) {
        this.phno = phno;
    }
    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }


}