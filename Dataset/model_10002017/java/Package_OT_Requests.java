




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Package_OT_Requests  {

    private LocalDate OtDay;
    private int id;
    private int OTType;
    private int EmpID;





    private Package_Employee package_employee;


    public Package_OT_Requests(
        LocalDate OtDay,        int id,        int OTType,        int EmpID    ) {
        this.OtDay = OtDay;
        this.id = id;
        this.OTType = OTType;
        this.EmpID = EmpID;
    }


    public LocalDate getOtday() {
        return OtDay;
    }

    public void setOtday(LocalDate OtDay) {
        this.OtDay = OtDay;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getOttype() {
        return OTType;
    }

    public void setOttype(int OTType) {
        this.OTType = OTType;
    }
    public int getEmpid() {
        return EmpID;
    }

    public void setEmpid(int EmpID) {
        this.EmpID = EmpID;
    }

    public Package_Employee getPackage_employee() {
        return package_employee;
    }

    public void setPackage_employee(Package_Employee package_employee) {
        this.package_employee = package_employee;
    }

}