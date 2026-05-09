





import java.util.List;
import java.util.ArrayList;

public class myAtl_SimpleOutPatternElement extends OutPatternElement {

    private String varName;





    private myAtl_ATLType myatl_atltype;


    public myAtl_SimpleOutPatternElement(
        String varName    ) {
        super(
        );
        this.varName = varName;
    }


    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }

    public myAtl_ATLType getMyatl_atltype() {
        return myatl_atltype;
    }

    public void setMyatl_atltype(myAtl_ATLType myatl_atltype) {
        this.myatl_atltype = myatl_atltype;
    }

}