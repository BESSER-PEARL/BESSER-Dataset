





import java.util.List;
import java.util.ArrayList;

public class state_State extends NamedElement, Vertex {

    private boolean isSimple;
    private boolean isComposite;



    public state_State(
        boolean isSimple,        boolean isComposite    ) {
        super(
        );
        this.isSimple = isSimple;
        this.isComposite = isComposite;
    }


    public boolean getIssimple() {
        return isSimple;
    }

    public void setIssimple(boolean isSimple) {
        this.isSimple = isSimple;
    }
    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }


}