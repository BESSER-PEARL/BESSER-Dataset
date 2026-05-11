





import java.util.List;
import java.util.ArrayList;

public class miniJava_Method extends Member {

    private boolean isabstract;
    private boolean isstatic;





    private miniJava_MethodCall minijava_methodcall;


    public miniJava_Method(
        boolean isabstract,        boolean isstatic    ) {
        super(
        );
        this.isabstract = isabstract;
        this.isstatic = isstatic;
    }


    public boolean getIsabstract() {
        return isabstract;
    }

    public void setIsabstract(boolean isabstract) {
        this.isabstract = isabstract;
    }
    public boolean getIsstatic() {
        return isstatic;
    }

    public void setIsstatic(boolean isstatic) {
        this.isstatic = isstatic;
    }

    public miniJava_MethodCall getMinijava_methodcall() {
        return minijava_methodcall;
    }

    public void setMinijava_methodcall(miniJava_MethodCall minijava_methodcall) {
        this.minijava_methodcall = minijava_methodcall;
    }

}