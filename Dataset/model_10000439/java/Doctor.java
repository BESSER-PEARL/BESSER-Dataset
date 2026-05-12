





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String name;
    private String address;
    private String department;
    private String phno;
    private int docid;
    private String specialization;



    public Doctor(
        String name,        String address,        String department,        String phno,        int docid,        String specialization    ) {
        this.name = name;
        this.address = address;
        this.department = department;
        this.phno = phno;
        this.docid = docid;
        this.specialization = specialization;
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
    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }
    public String getPhno() {
        return phno;
    }

    public void setPhno(String phno) {
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


}