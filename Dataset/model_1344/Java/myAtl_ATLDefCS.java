





import java.util.List;
import java.util.ArrayList;

public class myAtl_ATLDefCS  {

    private String varName;





    private myAtl_Helper myatl_helper;




    private List<myAtl_ATLParameterCS> myatl_atlparametercss;




    private myAtl_ExpCS myatl_expcs;


    public myAtl_ATLDefCS(
        String varName    ) {
        this.varName = varName;
        this.myatl_atlparametercss = new ArrayList<>();
    }

    public myAtl_ATLDefCS(
        String varName        ArrayList<myAtl_ATLParameterCS> myatl_atlparametercss    ) {
        this.varName = varName;
        this.myatl_atlparametercss = myatl_atlparametercss;
    }

    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }

    public myAtl_Helper getMyatl_helper() {
        return myatl_helper;
    }

    public void setMyatl_helper(myAtl_Helper myatl_helper) {
        this.myatl_helper = myatl_helper;
    }
    public List<myAtl_ATLParameterCS> getMyatl_atlparametercss() {
        return myatl_atlparametercss;
    }

    public void addMyatl_atlparametercs(Myatl_atlparametercs myatl_atlparametercs) {
        this.myatl_atlparametercss.add(myatl_atlparametercs);
    }
    public myAtl_ExpCS getMyatl_expcs() {
        return myatl_expcs;
    }

    public void setMyatl_expcs(myAtl_ExpCS myatl_expcs) {
        this.myatl_expcs = myatl_expcs;
    }

}