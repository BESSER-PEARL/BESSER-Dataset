





import java.util.List;
import java.util.ArrayList;

public class Package_Allowance  {

    private String emp_id;
    private int id;
    private String Effectivedate;



    public Package_Allowance(
        String emp_id,        int id,        String Effectivedate    ) {
        this.emp_id = emp_id;
        this.id = id;
        this.Effectivedate = Effectivedate;
    }


    public String getEmp_id() {
        return emp_id;
    }

    public void setEmp_id(String emp_id) {
        this.emp_id = emp_id;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getEffectivedate() {
        return Effectivedate;
    }

    public void setEffectivedate(String Effectivedate) {
        this.Effectivedate = Effectivedate;
    }


}