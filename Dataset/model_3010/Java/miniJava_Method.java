





import java.util.List;
import java.util.ArrayList;

public class miniJava_Method extends Member {

    private boolean isstatic;
    private boolean isabstract;



    public miniJava_Method(
        boolean isstatic,        boolean isabstract    ) {
        super(
        );
        this.isstatic = isstatic;
        this.isabstract = isabstract;
    }


    public boolean getIsstatic() {
        return isstatic;
    }

    public void setIsstatic(boolean isstatic) {
        this.isstatic = isstatic;
    }
    public boolean getIsabstract() {
        return isabstract;
    }

    public void setIsabstract(boolean isabstract) {
        this.isabstract = isabstract;
    }


}