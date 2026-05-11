





import java.util.List;
import java.util.ArrayList;

public class miniJava_Clazz extends TypeDeclaration {

    private boolean isabstract;





    private miniJava_Clazz minijava_clazz;




    private miniJava_ClazzToMethodMap minijava_clazztomethodmap;


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
    public miniJava_ClazzToMethodMap getMinijava_clazztomethodmap() {
        return minijava_clazztomethodmap;
    }

    public void setMinijava_clazztomethodmap(miniJava_ClazzToMethodMap minijava_clazztomethodmap) {
        this.minijava_clazztomethodmap = minijava_clazztomethodmap;
    }

}