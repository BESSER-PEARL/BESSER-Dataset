





import java.util.List;
import java.util.ArrayList;

public class DOM_MethodInvocation extends Expression {






    private IMethod imethod;




    private List<Type> types;




    private SimpleName simplename;


    public DOM_MethodInvocation(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public DOM_MethodInvocation(
        ArrayList<Type> types    ) {
        this.types = types;
    }


    public IMethod getImethod() {
        return imethod;
    }

    public void setImethod(IMethod imethod) {
        this.imethod = imethod;
    }
    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }
    public SimpleName getSimplename() {
        return simplename;
    }

    public void setSimplename(SimpleName simplename) {
        this.simplename = simplename;
    }

}