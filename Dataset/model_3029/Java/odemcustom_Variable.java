





import java.util.List;
import java.util.ArrayList;

public class odemcustom_Variable extends Statement, AbstractVariable, ModifierExtensionsContainer {

    private boolean clazz;
    private boolean control;





    private odemcustom_Module odemcustom_module;




    private odemcustom_Annotation odemcustom_annotation;




    private odemcustom_ClassSimilar odemcustom_classsimilar;


    public odemcustom_Variable(
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

    public odemcustom_Module getOdemcustom_module() {
        return odemcustom_module;
    }

    public void setOdemcustom_module(odemcustom_Module odemcustom_module) {
        this.odemcustom_module = odemcustom_module;
    }
    public odemcustom_Annotation getOdemcustom_annotation() {
        return odemcustom_annotation;
    }

    public void setOdemcustom_annotation(odemcustom_Annotation odemcustom_annotation) {
        this.odemcustom_annotation = odemcustom_annotation;
    }
    public odemcustom_ClassSimilar getOdemcustom_classsimilar() {
        return odemcustom_classsimilar;
    }

    public void setOdemcustom_classsimilar(odemcustom_ClassSimilar odemcustom_classsimilar) {
        this.odemcustom_classsimilar = odemcustom_classsimilar;
    }

}