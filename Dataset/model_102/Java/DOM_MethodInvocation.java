





import java.util.List;
import java.util.ArrayList;

public class DOM_MethodInvocation extends Expression {






    private SimpleName simplename;




    private IMethod imethod;


    public DOM_MethodInvocation(
    ) {
        super(
        );
    }



    public SimpleName getSimplename() {
        return simplename;
    }

    public void setSimplename(SimpleName simplename) {
        this.simplename = simplename;
    }
    public IMethod getImethod() {
        return imethod;
    }

    public void setImethod(IMethod imethod) {
        this.imethod = imethod;
    }

}