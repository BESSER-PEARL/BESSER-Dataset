





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Advances  {

    private int id;
    private int remain;
    private int empid;
    private String amount;
    private int installments;





    private Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee;


    public Class_Diagram_for_Propsed_System_Advances(
        int id,        int remain,        int empid,        String amount,        int installments    ) {
        this.id = id;
        this.remain = remain;
        this.empid = empid;
        this.amount = amount;
        this.installments = installments;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getRemain() {
        return remain;
    }

    public void setRemain(int remain) {
        this.remain = remain;
    }
    public int getEmpid() {
        return empid;
    }

    public void setEmpid(int empid) {
        this.empid = empid;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }
    public int getInstallments() {
        return installments;
    }

    public void setInstallments(int installments) {
        this.installments = installments;
    }

    public Class_Diagram_for_Propsed_System_Employee getClass_diagram_for_propsed_system_employee() {
        return class_diagram_for_propsed_system_employee;
    }

    public void setClass_diagram_for_propsed_system_employee(Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee) {
        this.class_diagram_for_propsed_system_employee = class_diagram_for_propsed_system_employee;
    }

}