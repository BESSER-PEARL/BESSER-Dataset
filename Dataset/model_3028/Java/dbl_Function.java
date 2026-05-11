





import java.util.List;
import java.util.ArrayList;

public class dbl_Function extends TypedElement, NamedElement, LocalScope {

    private boolean class_;
    private boolean detached;
    private boolean abstract;



    public dbl_Function(
        boolean class_,        boolean detached,        boolean abstract    ) {
        super(
        );
        this.class_ = class_;
        this.detached = detached;
        this.abstract = abstract;
    }


    public boolean getClass_() {
        return class_;
    }

    public void setClass_(boolean class_) {
        this.class_ = class_;
    }
    public boolean getDetached() {
        return detached;
    }

    public void setDetached(boolean detached) {
        this.detached = detached;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }


}