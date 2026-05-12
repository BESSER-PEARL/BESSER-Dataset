





import java.util.List;
import java.util.ArrayList;

public class XHTML_Td extends Attrs, Cellhalign, TrElement, Cellvalign {

    private String scope;



    public XHTML_Td(
        String scope    ) {
        super(
        );
        this.scope = scope;
    }


    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }


}