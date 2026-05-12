





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String EmpLName;
    private String State;
    private String City;
    private String Gender;
    private String EmpFName;
    private String EmpType;
    private String Department;
    private String DOB;
    private int EmpId;
    private String Zipcode;
    private String Address;



    public Employee(
        String EmpLName,        String State,        String City,        String Gender,        String EmpFName,        String EmpType,        String Department,        String DOB,        int EmpId,        String Zipcode,        String Address    ) {
        this.EmpLName = EmpLName;
        this.State = State;
        this.City = City;
        this.Gender = Gender;
        this.EmpFName = EmpFName;
        this.EmpType = EmpType;
        this.Department = Department;
        this.DOB = DOB;
        this.EmpId = EmpId;
        this.Zipcode = Zipcode;
        this.Address = Address;
    }


    public String getEmplname() {
        return EmpLName;
    }

    public void setEmplname(String EmpLName) {
        this.EmpLName = EmpLName;
    }
    public String getState() {
        return State;
    }

    public void setState(String State) {
        this.State = State;
    }
    public String getCity() {
        return City;
    }

    public void setCity(String City) {
        this.City = City;
    }
    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }
    public String getEmpfname() {
        return EmpFName;
    }

    public void setEmpfname(String EmpFName) {
        this.EmpFName = EmpFName;
    }
    public String getEmptype() {
        return EmpType;
    }

    public void setEmptype(String EmpType) {
        this.EmpType = EmpType;
    }
    public String getDepartment() {
        return Department;
    }

    public void setDepartment(String Department) {
        this.Department = Department;
    }
    public String getDob() {
        return DOB;
    }

    public void setDob(String DOB) {
        this.DOB = DOB;
    }
    public int getEmpid() {
        return EmpId;
    }

    public void setEmpid(int EmpId) {
        this.EmpId = EmpId;
    }
    public String getZipcode() {
        return Zipcode;
    }

    public void setZipcode(String Zipcode) {
        this.Zipcode = Zipcode;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }


}