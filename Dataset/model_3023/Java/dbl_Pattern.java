





import java.util.List;
import java.util.ArrayList;

public class dbl_Pattern extends NamedElement {

    private boolean top;





    private dbl_ReferencePropertyType dbl_referencepropertytype;


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

    public dbl_ReferencePropertyType getDbl_referencepropertytype() {
        return dbl_referencepropertytype;
    }

    public void setDbl_referencepropertytype(dbl_ReferencePropertyType dbl_referencepropertytype) {
        this.dbl_referencepropertytype = dbl_referencepropertytype;
    }

}