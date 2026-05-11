





import java.util.List;
import java.util.ArrayList;

public class odemcustom_SetGenContextStatement extends SimpleStatement {

    private boolean addAfterContext;





    private odemcustom_Expression odemcustom_expression;


    public odemcustom_SetGenContextStatement(
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

    public odemcustom_Expression getOdemcustom_expression() {
        return odemcustom_expression;
    }

    public void setOdemcustom_expression(odemcustom_Expression odemcustom_expression) {
        this.odemcustom_expression = odemcustom_expression;
    }

}