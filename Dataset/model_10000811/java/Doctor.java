





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String name;
    private int phno;
    private int docid;
    private String specialization;
    private String department;
    private String address;



    public Doctor(
        String name,        int phno,        int docid,        String specialization,        String department,        String address    ) {
        this.name = name;
        this.phno = phno;
        this.docid = docid;
        this.specialization = specialization;
        this.department = department;
        this.address = address;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}