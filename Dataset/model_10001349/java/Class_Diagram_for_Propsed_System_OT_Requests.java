




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_OT_Requests  {

    private int EmpID;
    private int OTType;
    private int id;
    private LocalDate OtDay;





    private Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee;


    public Class_Diagram_for_Propsed_System_OT_Requests(
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

    public Class_Diagram_for_Propsed_System_Employee getClass_diagram_for_propsed_system_employee() {
        return class_diagram_for_propsed_system_employee;
    }

    public void setClass_diagram_for_propsed_system_employee(Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee) {
        this.class_diagram_for_propsed_system_employee = class_diagram_for_propsed_system_employee;
    }

}