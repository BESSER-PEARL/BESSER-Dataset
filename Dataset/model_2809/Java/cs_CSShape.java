





import java.util.List;
import java.util.ArrayList;

public class cs_CSShape extends ENamedElement {

    private boolean closed;





    private cs_CSElement cs_cselement;


    public cs_CSShape(
        boolean closed    ) {
        super(
        );
        this.closed = closed;
    }


    public boolean getClosed() {
        return closed;
    }

    public void setClosed(boolean closed) {
        this.closed = closed;
    }

    public cs_CSElement getCs_cselement() {
        return cs_cselement;
    }

    public void setCs_cselement(cs_CSElement cs_cselement) {
        this.cs_cselement = cs_cselement;
    }

}