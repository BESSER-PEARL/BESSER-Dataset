





import java.util.List;
import java.util.ArrayList;

public class miniJava_Clazz extends TypeDeclaration {

    private boolean isabstract;





    private miniJava_Clazz minijava_clazz;




    private miniJava_NewObject minijava_newobject;




    private miniJava_ObjectInstance minijava_objectinstance;


    public miniJava_Clazz(
        boolean isabstract    ) {
        super(
        );
        this.isabstract = isabstract;
    }


    public boolean getIsabstract() {
        return isabstract;
    }

    public void setIsabstract(boolean isabstract) {
        this.isabstract = isabstract;
    }

    public miniJava_Clazz getMinijava_clazz() {
        return minijava_clazz;
    }

    public void setMinijava_clazz(miniJava_Clazz minijava_clazz) {
        this.minijava_clazz = minijava_clazz;
    }
    public miniJava_NewObject getMinijava_newobject() {
        return minijava_newobject;
    }

    public void setMinijava_newobject(miniJava_NewObject minijava_newobject) {
        this.minijava_newobject = minijava_newobject;
    }
    public miniJava_ObjectInstance getMinijava_objectinstance() {
        return minijava_objectinstance;
    }

    public void setMinijava_objectinstance(miniJava_ObjectInstance minijava_objectinstance) {
        this.minijava_objectinstance = minijava_objectinstance;
    }

}