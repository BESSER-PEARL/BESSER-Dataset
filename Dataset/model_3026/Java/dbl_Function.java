





import java.util.List;
import java.util.ArrayList;

public class dbl_Function extends NamedElement, LocalScope, TypedElement {

    private boolean class_;
    private boolean abstract;



    public dbl_Function(
        boolean class_,        boolean abstract    ) {
        super(
        );
        this.class_ = class_;
        this.abstract = abstract;
    }


    public boolean getClass_() {
        return class_;
    }

    public void setClass_(boolean class_) {
        this.class_ = class_;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }


}