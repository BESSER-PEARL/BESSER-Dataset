





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private int docid;
    private String specialization;
    private int phno;
    private String department;
    private String name;
    private String address;



    public Doctor(
        int docid,        String specialization,        int phno,        String department,        String name,        String address    ) {
        this.docid = docid;
        this.specialization = specialization;
        this.phno = phno;
        this.department = department;
        this.name = name;
        this.address = address;
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


}