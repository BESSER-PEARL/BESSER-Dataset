





import java.util.List;
import java.util.ArrayList;

public class myAtl_InPatternElement  {

    private String varName;





    private myAtl_InPattern myatl_inpattern;




    private myAtl_ATLType myatl_atltype;


    public myAtl_InPatternElement(
        String varName    ) {
        this.varName = varName;
    }


    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }

    public myAtl_InPattern getMyatl_inpattern() {
        return myatl_inpattern;
    }

    public void setMyatl_inpattern(myAtl_InPattern myatl_inpattern) {
        this.myatl_inpattern = myatl_inpattern;
    }
    public myAtl_ATLType getMyatl_atltype() {
        return myatl_atltype;
    }

    public void setMyatl_atltype(myAtl_ATLType myatl_atltype) {
        this.myatl_atltype = myatl_atltype;
    }

}