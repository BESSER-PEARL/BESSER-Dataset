





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Proposed_system_Advances  {

    private String salaryId;
    private String amount;
    private String issueDate;
    private String installments;
    private String id;





    private List<Class_Diagram_for_Proposed_system_Salary> class_diagram_for_proposed_system_salarys;


    public Class_Diagram_for_Proposed_system_Advances(
        String salaryId,        String amount,        String issueDate,        String installments,        String id    ) {
        this.salaryId = salaryId;
        this.amount = amount;
        this.issueDate = issueDate;
        this.installments = installments;
        this.id = id;
        this.class_diagram_for_proposed_system_salarys = new ArrayList<>();
    }

    public Class_Diagram_for_Proposed_system_Advances(
        String salaryId,        String amount,        String issueDate,        String installments,        String id        ArrayList<Class_Diagram_for_Proposed_system_Salary> class_diagram_for_proposed_system_salarys    ) {
        this.salaryId = salaryId;
        this.amount = amount;
        this.issueDate = issueDate;
        this.installments = installments;
        this.id = id;
        this.class_diagram_for_proposed_system_salarys = class_diagram_for_proposed_system_salarys;
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
    public String getIssuedate() {
        return issueDate;
    }

    public void setIssuedate(String issueDate) {
        this.issueDate = issueDate;
    }
    public String getInstallments() {
        return installments;
    }

    public void setInstallments(String installments) {
        this.installments = installments;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<Class_Diagram_for_Proposed_system_Salary> getClass_diagram_for_proposed_system_salarys() {
        return class_diagram_for_proposed_system_salarys;
    }

    public void addClass_diagram_for_proposed_system_salary(Class_diagram_for_proposed_system_salary class_diagram_for_proposed_system_salary) {
        this.class_diagram_for_proposed_system_salarys.add(class_diagram_for_proposed_system_salary);
    }

}