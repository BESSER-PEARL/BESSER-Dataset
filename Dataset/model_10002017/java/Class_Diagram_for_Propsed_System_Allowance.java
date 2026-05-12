





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Allowance  {

    private int emp_id;
    private String effectivedate;
    private String amount;
    private int id;



    public Class_Diagram_for_Propsed_System_Allowance(
        int emp_id,        String effectivedate,        String amount,        int id    ) {
        this.emp_id = emp_id;
        this.effectivedate = effectivedate;
        this.amount = amount;
        this.id = id;
    }


    public int getEmp_id() {
        return emp_id;
    }

    public void setEmp_id(int emp_id) {
        this.emp_id = emp_id;
    }
    public String getEffectivedate() {
        return effectivedate;
    }

    public void setEffectivedate(String effectivedate) {
        this.effectivedate = effectivedate;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}