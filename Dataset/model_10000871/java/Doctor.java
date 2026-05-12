





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private int docid;
    private int phno;
    private String name;
    private String address;
    private String department;
    private int departamentID;
    private String specialization;



    public Doctor(
        int docid,        int phno,        String name,        String address,        String department,        int departamentID,        String specialization    ) {
        this.docid = docid;
        this.phno = phno;
        this.name = name;
        this.address = address;
        this.department = department;
        this.departamentID = departamentID;
        this.specialization = specialization;
    }


    public int getDocid() {
        return docid;
    }

    public void setDocid(int docid) {
        this.docid = docid;
    }
    public int getPhno() {
        return phno;
    }

    public void setPhno(int phno) {
        this.phno = phno;
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
    public int getDepartamentid() {
        return departamentID;
    }

    public void setDepartamentid(int departamentID) {
        this.departamentID = departamentID;
    }
    public String getSpecialization() {
        return specialization;
    }

    public void setSpecialization(String specialization) {
        this.specialization = specialization;
    }


}