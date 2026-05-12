





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String address;
    private String name;
    private int docid;
    private String specialization;
    private String department;
    private int phno;



    public Doctor(
        String address,        String name,        int docid,        String specialization,        String department,        int phno    ) {
        this.address = address;
        this.name = name;
        this.docid = docid;
        this.specialization = specialization;
        this.department = department;
        this.phno = phno;
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
    public int getPhno() {
        return phno;
    }

    public void setPhno(int phno) {
        this.phno = phno;
    }


}