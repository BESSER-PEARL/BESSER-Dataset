





import java.util.List;
import java.util.ArrayList;

public class dbl_SetGenContextStatement extends SimpleStatement {

    private boolean addAfterContext;





    private dbl_Expression dbl_expression;


    public dbl_SetGenContextStatement(
        boolean addAfterContext    ) {
        super(
        );
        this.addAfterContext = addAfterContext;
    }


    public boolean getAddaftercontext() {
        return addAfterContext;
    }

    public void setAddaftercontext(boolean addAfterContext) {
        this.addAfterContext = addAfterContext;
    }

    public dbl_Expression getDbl_expression() {
        return dbl_expression;
    }

    public void setDbl_expression(dbl_Expression dbl_expression) {
        this.dbl_expression = dbl_expression;
    }

}