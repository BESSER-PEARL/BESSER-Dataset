





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Allowance  {

    private String effectivedate;
    private int emp_id;
    private int id;
    private String amount;



    public Class_Diagram_for_Propsed_System_Allowance(
        String effectivedate,        int emp_id,        int id,        String amount    ) {
        this.effectivedate = effectivedate;
        this.emp_id = emp_id;
        this.id = id;
        this.amount = amount;
    }


    public String getEffectivedate() {
        return effectivedate;
    }

    public void setEffectivedate(String effectivedate) {
        this.effectivedate = effectivedate;
    }
    public int getEmp_id() {
        return emp_id;
    }

    public void setEmp_id(int emp_id) {
        this.emp_id = emp_id;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }


}