





import java.util.List;
import java.util.ArrayList;

public class myAtl_Binding  {

    private String propertyName;





    private myAtl_ExpCS myatl_expcs;




    private myAtl_SimpleOutPatternElement myatl_simpleoutpatternelement;


    public myAtl_Binding(
        String propertyName    ) {
        this.propertyName = propertyName;
    }


    public String getPropertyname() {
        return propertyName;
    }

    public void setPropertyname(String propertyName) {
        this.propertyName = propertyName;
    }

    public myAtl_ExpCS getMyatl_expcs() {
        return myatl_expcs;
    }

    public void setMyatl_expcs(myAtl_ExpCS myatl_expcs) {
        this.myatl_expcs = myatl_expcs;
    }
    public myAtl_SimpleOutPatternElement getMyatl_simpleoutpatternelement() {
        return myatl_simpleoutpatternelement;
    }

    public void setMyatl_simpleoutpatternelement(myAtl_SimpleOutPatternElement myatl_simpleoutpatternelement) {
        this.myatl_simpleoutpatternelement = myatl_simpleoutpatternelement;
    }

}