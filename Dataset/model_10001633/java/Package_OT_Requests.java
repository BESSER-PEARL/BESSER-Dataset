




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Package_OT_Requests  {

    private int EmpID;
    private int OTType;
    private int id;
    private LocalDate OtDay;





    private Package_Employee package_employee;


    public Package_OT_Requests(
        int EmpID,        int OTType,        int id,        LocalDate OtDay    ) {
        this.EmpID = EmpID;
        this.OTType = OTType;
        this.id = id;
        this.OtDay = OtDay;
    }


    public int getEmpid() {
        return EmpID;
    }

    public void setEmpid(int EmpID) {
        this.EmpID = EmpID;
    }
    public int getOttype() {
        return OTType;
    }

    public void setOttype(int OTType) {
        this.OTType = OTType;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public LocalDate getOtday() {
        return OtDay;
    }

    public void setOtday(LocalDate OtDay) {
        this.OtDay = OtDay;
    }

    public Package_Employee getPackage_employee() {
        return package_employee;
    }

    public void setPackage_employee(Package_Employee package_employee) {
        this.package_employee = package_employee;
    }

}