





import java.util.List;
import java.util.ArrayList;

public class atem_Driver  {

    private String dsl_Driver_RegEx;
    private String dsl_Driver_Status;





    private atem_AtemModel atem_atemmodel;


    public atem_Driver(
        String dsl_Driver_RegEx,        String dsl_Driver_Status    ) {
        this.dsl_Driver_RegEx = dsl_Driver_RegEx;
        this.dsl_Driver_Status = dsl_Driver_Status;
    }


    public String getDsl_driver_regex() {
        return dsl_Driver_RegEx;
    }

    public void setDsl_driver_regex(String dsl_Driver_RegEx) {
        this.dsl_Driver_RegEx = dsl_Driver_RegEx;
    }
    public String getDsl_driver_status() {
        return dsl_Driver_Status;
    }

    public void setDsl_driver_status(String dsl_Driver_Status) {
        this.dsl_Driver_Status = dsl_Driver_Status;
    }

    public atem_AtemModel getAtem_atemmodel() {
        return atem_atemmodel;
    }

    public void setAtem_atemmodel(atem_AtemModel atem_atemmodel) {
        this.atem_atemmodel = atem_atemmodel;
    }

}