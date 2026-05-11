





import java.util.List;
import java.util.ArrayList;

public class dbl_Variable extends ModifierExtensionsContainer, AbstractVariable, Statement {

    private boolean control;
    private boolean clazz;





    private dbl_ClassSimilar dbl_classsimilar;




    private dbl_Annotation dbl_annotation;




    private dbl_Module dbl_module;


    public dbl_Variable(
        boolean control,        boolean clazz    ) {
        super(
        );
        this.control = control;
        this.clazz = clazz;
    }


    public boolean getControl() {
        return control;
    }

    public void setControl(boolean control) {
        this.control = control;
    }
    public boolean getClazz() {
        return clazz;
    }

    public void setClazz(boolean clazz) {
        this.clazz = clazz;
    }

    public dbl_ClassSimilar getDbl_classsimilar() {
        return dbl_classsimilar;
    }

    public void setDbl_classsimilar(dbl_ClassSimilar dbl_classsimilar) {
        this.dbl_classsimilar = dbl_classsimilar;
    }
    public dbl_Annotation getDbl_annotation() {
        return dbl_annotation;
    }

    public void setDbl_annotation(dbl_Annotation dbl_annotation) {
        this.dbl_annotation = dbl_annotation;
    }
    public dbl_Module getDbl_module() {
        return dbl_module;
    }

    public void setDbl_module(dbl_Module dbl_module) {
        this.dbl_module = dbl_module;
    }

}