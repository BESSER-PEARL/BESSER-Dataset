





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Deductions  {

    private String amount;
    private String id;
    private int empid;



    public Class_Diagram_for_Propsed_System_Deductions(
        String amount,        String id,        int empid    ) {
        this.amount = amount;
        this.id = id;
        this.empid = empid;
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
    public int getEmpid() {
        return empid;
    }

    public void setEmpid(int empid) {
        this.empid = empid;
    }


}