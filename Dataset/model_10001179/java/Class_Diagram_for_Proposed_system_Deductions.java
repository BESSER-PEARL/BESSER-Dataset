





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Proposed_system_Deductions  {

    private String deducType;
    private String deductDate;
    private String amount;
    private String id;
    private String salaryId;





    private Class_Diagram_for_Proposed_system_Salary class_diagram_for_proposed_system_salary;


    public Class_Diagram_for_Proposed_system_Deductions(
        String deducType,        String deductDate,        String amount,        String id,        String salaryId    ) {
        this.deducType = deducType;
        this.deductDate = deductDate;
        this.amount = amount;
        this.id = id;
        this.salaryId = salaryId;
    }


    public String getDeductype() {
        return deducType;
    }

    public void setDeductype(String deducType) {
        this.deducType = deducType;
    }
    public String getDeductdate() {
        return deductDate;
    }

    public void setDeductdate(String deductDate) {
        this.deductDate = deductDate;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSalaryid() {
        return salaryId;
    }

    public void setSalaryid(String salaryId) {
        this.salaryId = salaryId;
    }

    public Class_Diagram_for_Proposed_system_Salary getClass_diagram_for_proposed_system_salary() {
        return class_diagram_for_proposed_system_salary;
    }

    public void setClass_diagram_for_proposed_system_salary(Class_Diagram_for_Proposed_system_Salary class_diagram_for_proposed_system_salary) {
        this.class_diagram_for_proposed_system_salary = class_diagram_for_proposed_system_salary;
    }

}