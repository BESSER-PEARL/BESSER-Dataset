





import java.util.List;
import java.util.ArrayList;

public class myDsl_constant  {

    private String enumt;
    private String i_constant;
    private String f_constant;



    public myDsl_constant(
        String enumt,        String i_constant,        String f_constant    ) {
        this.enumt = enumt;
        this.i_constant = i_constant;
        this.f_constant = f_constant;
    }


    public String getEnumt() {
        return enumt;
    }

    public void setEnumt(String enumt) {
        this.enumt = enumt;
    }
    public String getI_constant() {
        return i_constant;
    }

    public void setI_constant(String i_constant) {
        this.i_constant = i_constant;
    }
    public String getF_constant() {
        return f_constant;
    }

    public void setF_constant(String f_constant) {
        this.f_constant = f_constant;
    }


}