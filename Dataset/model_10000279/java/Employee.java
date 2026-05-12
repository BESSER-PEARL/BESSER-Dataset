





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String jopType;
    private String Name;
    private String Contact_;
    private int EmpID;



    public Employee(
        String jopType,        String Name,        String Contact_,        int EmpID    ) {
        this.jopType = jopType;
        this.Name = Name;
        this.Contact_ = Contact_;
        this.EmpID = EmpID;
    }


    public String getJoptype() {
        return jopType;
    }

    public void setJoptype(String jopType) {
        this.jopType = jopType;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getContact_() {
        return Contact_;
    }

    public void setContact_(String Contact_) {
        this.Contact_ = Contact_;
    }
    public int getEmpid() {
        return EmpID;
    }

    public void setEmpid(int EmpID) {
        this.EmpID = EmpID;
    }


}