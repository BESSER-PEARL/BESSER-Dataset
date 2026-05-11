





import java.util.List;
import java.util.ArrayList;

public class miniJava_Method extends Member {

    private boolean static;
    private boolean abstract;



    public miniJava_Method(
        boolean static,        boolean abstract    ) {
        super(
        );
        this.static = static;
        this.abstract = abstract;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }


}