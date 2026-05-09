





import java.util.List;
import java.util.ArrayList;

public class myAtl_ATLParameterCS  {

    private String varName;





    private myAtl_QueryRule myatl_queryrule;


    public myAtl_ATLParameterCS(
        String varName    ) {
        this.varName = varName;
    }


    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }

    public myAtl_QueryRule getMyatl_queryrule() {
        return myatl_queryrule;
    }

    public void setMyatl_queryrule(myAtl_QueryRule myatl_queryrule) {
        this.myatl_queryrule = myatl_queryrule;
    }

}