





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String name;
    private String department;
    private int docid;
    private String address;
    private int phno;
    private String specialization;



    public Doctor(
        String name,        String department,        int docid,        String address,        int phno,        String specialization    ) {
        this.name = name;
        this.department = department;
        this.docid = docid;
        this.address = address;
        this.phno = phno;
        this.specialization = specialization;
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


}