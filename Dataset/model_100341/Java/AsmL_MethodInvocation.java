





import java.util.List;
import java.util.ArrayList;

public class AsmL_MethodInvocation extends Rule {






    private MethodCallTerm methodcallterm;


    public AsmL_MethodInvocation(
    ) {
        super(
        );
    }



    public MethodCallTerm getMethodcallterm() {
        return methodcallterm;
    }

    public void setMethodcallterm(MethodCallTerm methodcallterm) {
        this.methodcallterm = methodcallterm;
    }

}