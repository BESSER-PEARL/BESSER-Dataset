





import java.util.List;
import java.util.ArrayList;

public class fsmtest_TransitionDeclaration  {

    private String name;





    private fsmtest_SignalDeclaration fsmtest_signaldeclaration;


    public fsmtest_TransitionDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fsmtest_SignalDeclaration getFsmtest_signaldeclaration() {
        return fsmtest_signaldeclaration;
    }

    public void setFsmtest_signaldeclaration(fsmtest_SignalDeclaration fsmtest_signaldeclaration) {
        this.fsmtest_signaldeclaration = fsmtest_signaldeclaration;
    }

}