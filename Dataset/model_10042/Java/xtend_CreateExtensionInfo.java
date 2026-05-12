





import java.util.List;
import java.util.ArrayList;

public class xtend_CreateExtensionInfo  {

    private String name;





    private xtend_XtendFunction xtend_xtendfunction;




    private xtend_XExpression xtend_xexpression;


    public xtend_CreateExtensionInfo(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public xtend_XtendFunction getXtend_xtendfunction() {
        return xtend_xtendfunction;
    }

    public void setXtend_xtendfunction(xtend_XtendFunction xtend_xtendfunction) {
        this.xtend_xtendfunction = xtend_xtendfunction;
    }
    public xtend_XExpression getXtend_xexpression() {
        return xtend_xexpression;
    }

    public void setXtend_xexpression(xtend_XExpression xtend_xexpression) {
        this.xtend_xexpression = xtend_xexpression;
    }

}