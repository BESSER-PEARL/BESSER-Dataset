





import java.util.List;
import java.util.ArrayList;

public class JavaSimplified_MethodCall  {






    private JavaSimplified_Name javasimplified_name;




    private JavaSimplified_MethodInvocation javasimplified_methodinvocation;




    private List<JavaSimplified_Expression> javasimplified_expressions;




    private List<JavaSimplified_MethodCall> javasimplified_methodcalls;


    public JavaSimplified_MethodCall(
    ) {
        this.javasimplified_expressions = new ArrayList<>();
        this.javasimplified_methodcalls = new ArrayList<>();
    }

    public JavaSimplified_MethodCall(
        ArrayList<JavaSimplified_Expression> javasimplified_expressions,        ArrayList<JavaSimplified_MethodCall> javasimplified_methodcalls    ) {
        this.javasimplified_expressions = javasimplified_expressions;
        this.javasimplified_methodcalls = javasimplified_methodcalls;
    }


    public JavaSimplified_Name getJavasimplified_name() {
        return javasimplified_name;
    }

    public void setJavasimplified_name(JavaSimplified_Name javasimplified_name) {
        this.javasimplified_name = javasimplified_name;
    }
    public JavaSimplified_MethodInvocation getJavasimplified_methodinvocation() {
        return javasimplified_methodinvocation;
    }

    public void setJavasimplified_methodinvocation(JavaSimplified_MethodInvocation javasimplified_methodinvocation) {
        this.javasimplified_methodinvocation = javasimplified_methodinvocation;
    }
    public List<JavaSimplified_Expression> getJavasimplified_expressions() {
        return javasimplified_expressions;
    }

    public void addJavasimplified_expression(Javasimplified_expression javasimplified_expression) {
        this.javasimplified_expressions.add(javasimplified_expression);
    }
    public List<JavaSimplified_MethodCall> getJavasimplified_methodcalls() {
        return javasimplified_methodcalls;
    }

    public void addJavasimplified_methodcall(Javasimplified_methodcall javasimplified_methodcall) {
        this.javasimplified_methodcalls.add(javasimplified_methodcall);
    }

}