





import java.util.List;
import java.util.ArrayList;

public class HSM_StateBase extends MgaObject {

    private String defaultTransition;
    private String marked;



    public HSM_StateBase(
        String defaultTransition,        String marked    ) {
        super(
        );
        this.defaultTransition = defaultTransition;
        this.marked = marked;
    }


    public String getDefaulttransition() {
        return defaultTransition;
    }

    public void setDefaulttransition(String defaultTransition) {
        this.defaultTransition = defaultTransition;
    }
    public String getMarked() {
        return marked;
    }

    public void setMarked(String marked) {
        this.marked = marked;
    }


}