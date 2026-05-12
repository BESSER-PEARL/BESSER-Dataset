





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String specialization;
    private String address;
    private int docid;
    private int phno;
    private String name;
    private String department;



    public Doctor(
        String specialization,        String address,        int docid,        int phno,        String name,        String department    ) {
        this.specialization = specialization;
        this.address = address;
        this.docid = docid;
        this.phno = phno;
        this.name = name;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }


}