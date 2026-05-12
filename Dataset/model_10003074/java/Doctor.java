





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String department;
    private String name;
    private String specialization;
    private int phno;
    private int docid;
    private String address;



    public Doctor(
        String department,        String name,        String specialization,        int phno,        int docid,        String address    ) {
        this.department = department;
        this.name = name;
        this.specialization = specialization;
        this.phno = phno;
        this.docid = docid;
        this.address = address;
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
    public int getDocid() {
        return docid;
    }

    public void setDocid(int docid) {
        this.docid = docid;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}