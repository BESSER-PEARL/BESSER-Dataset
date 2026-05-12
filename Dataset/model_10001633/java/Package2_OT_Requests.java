




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Package2_OT_Requests  {

    private LocalDate OtDay;
    private int id;
    private int EmpID;
    private int OTType;





    private Package2_Employee package2_employee;


    public Package2_OT_Requests(
        LocalDate OtDay,        int id,        int EmpID,        int OTType    ) {
        this.OtDay = OtDay;
        this.id = id;
        this.EmpID = EmpID;
        this.OTType = OTType;
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

    public Package2_Employee getPackage2_employee() {
        return package2_employee;
    }

    public void setPackage2_employee(Package2_Employee package2_employee) {
        this.package2_employee = package2_employee;
    }

}