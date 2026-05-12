





import java.util.List;
import java.util.ArrayList;

public class Package2_Allowance  {

    private String emp_id;
    private String Effectivedate;
    private int id;



    public Package2_Allowance(
        String emp_id,        String Effectivedate,        int id    ) {
        this.emp_id = emp_id;
        this.Effectivedate = Effectivedate;
        this.id = id;
    }


    public String getEmp_id() {
        return emp_id;
    }

    public void setEmp_id(String emp_id) {
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


}