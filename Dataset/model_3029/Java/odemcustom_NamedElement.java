





import java.util.List;
import java.util.ArrayList;

public class odemcustom_NamedElement extends ExpandableElement {

    private String name;





    private odemcustom_IdExpr odemcustom_idexpr;


    public odemcustom_NamedElement(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public odemcustom_IdExpr getOdemcustom_idexpr() {
        return odemcustom_idexpr;
    }

    public void setOdemcustom_idexpr(odemcustom_IdExpr odemcustom_idexpr) {
        this.odemcustom_idexpr = odemcustom_idexpr;
    }

}