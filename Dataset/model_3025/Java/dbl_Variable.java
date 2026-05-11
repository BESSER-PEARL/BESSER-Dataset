





import java.util.List;
import java.util.ArrayList;

public class dbl_Variable extends ModifierExtensionsContainer, AbstractVariable, SimpleStatement {

    private boolean clazz;
    private boolean control;





    private dbl_Module dbl_module;


    public dbl_Variable(
        boolean clazz,        boolean control    ) {
        super(
        );
        this.clazz = clazz;
        this.control = control;
    }


    public boolean getClazz() {
        return clazz;
    }

    public void setClazz(boolean clazz) {
        this.clazz = clazz;
    }
    public boolean getControl() {
        return control;
    }

    public void setControl(boolean control) {
        this.control = control;
    }

    public dbl_Module getDbl_module() {
        return dbl_module;
    }

    public void setDbl_module(dbl_Module dbl_module) {
        this.dbl_module = dbl_module;
    }

}