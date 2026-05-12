





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private int phno;
    private String address;
    private String department;
    private String name;
    private int docid;
    private String specialization;



    public Doctor(
        int phno,        String address,        String department,        String name,        int docid,        String specialization    ) {
        this.phno = phno;
        this.address = address;
        this.department = department;
        this.name = name;
        this.docid = docid;
        this.specialization = specialization;
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


}