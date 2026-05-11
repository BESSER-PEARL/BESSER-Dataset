





import java.util.List;
import java.util.ArrayList;

public class dbl_SetGenContextStatement extends SimpleStatement {

    private boolean addAfterContext;



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


}