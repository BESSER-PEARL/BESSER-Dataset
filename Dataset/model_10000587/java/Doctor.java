





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String department;
    private int docid;
    private String name;
    private int phno;
    private String specialization;
    private String address;



    public Doctor(
        String department,        int docid,        String name,        int phno,        String specialization,        String address    ) {
        this.department = department;
        this.docid = docid;
        this.name = name;
        this.phno = phno;
        this.specialization = specialization;
        this.address = address;
    }


    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}