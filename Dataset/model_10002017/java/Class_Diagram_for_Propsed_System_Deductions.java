





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Deductions  {

    private String amount;
    private int empid;
    private int id;



    public Class_Diagram_for_Propsed_System_Deductions(
        String amount,        int empid,        int id    ) {
        this.amount = amount;
        this.empid = empid;
        this.id = id;
    }


    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }
    public int getEmpid() {
        return empid;
    }

    public void setEmpid(int empid) {
        this.empid = empid;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}