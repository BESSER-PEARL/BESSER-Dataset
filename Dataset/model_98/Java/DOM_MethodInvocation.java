





import java.util.List;
import java.util.ArrayList;

public class DOM_MethodInvocation extends Expression {






    private IMethod imethod;




    private SimpleName simplename;


    public DOM_MethodInvocation(
    ) {
        super(
        );
    }



    public IMethod getImethod() {
        return imethod;
    }

    public void setImethod(IMethod imethod) {
        this.imethod = imethod;
    }
    public SimpleName getSimplename() {
        return simplename;
    }

    public void setSimplename(SimpleName simplename) {
        this.simplename = simplename;
    }

}