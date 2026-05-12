





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Proposed_system_Allowances  {

    private String salaryId;
    private String amount;
    private String allowanceType;
    private String id;
    private String issueDate;





    private Class_Diagram_for_Proposed_system_Salary class_diagram_for_proposed_system_salary;


    public Class_Diagram_for_Proposed_system_Allowances(
        String salaryId,        String amount,        String allowanceType,        String id,        String issueDate    ) {
        this.salaryId = salaryId;
        this.amount = amount;
        this.allowanceType = allowanceType;
        this.id = id;
        this.issueDate = issueDate;
    }


    public String getSalaryid() {
        return salaryId;
    }

    public void setSalaryid(String salaryId) {
        this.salaryId = salaryId;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }
    public String getAllowancetype() {
        return allowanceType;
    }

    public void setAllowancetype(String allowanceType) {
        this.allowanceType = allowanceType;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getIssuedate() {
        return issueDate;
    }

    public void setIssuedate(String issueDate) {
        this.issueDate = issueDate;
    }

    public Class_Diagram_for_Proposed_system_Salary getClass_diagram_for_proposed_system_salary() {
        return class_diagram_for_proposed_system_salary;
    }

    public void setClass_diagram_for_proposed_system_salary(Class_Diagram_for_Proposed_system_Salary class_diagram_for_proposed_system_salary) {
        this.class_diagram_for_proposed_system_salary = class_diagram_for_proposed_system_salary;
    }

}