





import java.util.List;
import java.util.ArrayList;

public class dbl_Variable extends AbstractVariable, SimpleStatement {

    private boolean control;
    private boolean class_;





    private dbl_Module dbl_module;




    private dbl_Class dbl_class;


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

    public dbl_Module getDbl_module() {
        return dbl_module;
    }

    public void setDbl_module(dbl_Module dbl_module) {
        this.dbl_module = dbl_module;
    }
    public dbl_Class getDbl_class() {
        return dbl_class;
    }

    public void setDbl_class(dbl_Class dbl_class) {
        this.dbl_class = dbl_class;
    }

}