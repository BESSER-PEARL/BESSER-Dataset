





import java.util.List;
import java.util.ArrayList;

public class Package_Allowance  {

    private String Effectivedate;
    private int id;
    private String emp_id;



    public Package_Allowance(
        String Effectivedate,        int id,        String emp_id    ) {
        this.Effectivedate = Effectivedate;
        this.id = id;
        this.emp_id = emp_id;
    }


    public String getEffectivedate() {
        return Effectivedate;
    }

    public void setEffectivedate(String Effectivedate) {
        this.Effectivedate = Effectivedate;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getEmp_id() {
        return emp_id;
    }

    public void setEmp_id(String emp_id) {
        this.emp_id = emp_id;
    }


}