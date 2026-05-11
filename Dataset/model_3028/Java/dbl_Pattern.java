





import java.util.List;
import java.util.ArrayList;

public class dbl_Pattern extends NamedElement {

    private boolean top;





    private dbl_Statement dbl_statement;


    public dbl_Pattern(
        boolean top    ) {
        super(
        );
        this.top = top;
    }


    public boolean getTop() {
        return top;
    }

    public void setTop(boolean top) {
        this.top = top;
    }

    public dbl_Statement getDbl_statement() {
        return dbl_statement;
    }

    public void setDbl_statement(dbl_Statement dbl_statement) {
        this.dbl_statement = dbl_statement;
    }

}