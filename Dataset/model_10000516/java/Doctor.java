





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String specialization;
    private int docid;
    private String department;
    private String name;
    private int phno;
    private String address;



    public Doctor(
        String specialization,        int docid,        String department,        String name,        int phno,        String address    ) {
        this.specialization = specialization;
        this.docid = docid;
        this.department = department;
        this.name = name;
        this.phno = phno;
        this.address = address;
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


}