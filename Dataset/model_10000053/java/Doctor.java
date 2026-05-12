





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String specialization;
    private String name;
    private String department;
    private String address;
    private int docid;
    private String phno;



    public Doctor(
        String specialization,        String name,        String department,        String address,        int docid,        String phno    ) {
        this.specialization = specialization;
        this.name = name;
        this.department = department;
        this.address = address;
        this.docid = docid;
        this.phno = phno;
    }


    public String getSpecialization() {
        return specialization;
    }

    public void setSpecialization(String specialization) {
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
    public String getPhno() {
        return phno;
    }

    public void setPhno(String phno) {
        this.phno = phno;
    }


}