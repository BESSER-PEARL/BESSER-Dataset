





import java.util.List;
import java.util.ArrayList;

public class dbl_Variable extends AbstractVariable, SimpleStatement {

    private boolean control;
    private boolean class_;



    public dbl_Variable(
        boolean control,        boolean class_    ) {
        super(
        );
        this.control = control;
        this.class_ = class_;
    }


    public boolean getControl() {
        return control;
    }

    public void setControl(boolean control) {
        this.control = control;
    }
    public boolean getClass_() {
        return class_;
    }

    public void setClass_(boolean class_) {
        this.class_ = class_;
    }


}