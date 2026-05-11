





import java.util.List;
import java.util.ArrayList;

public class JavaSimplified_MethodCall  {






    private JavaSimplified_MethodCall javasimplified_methodcall;




    private List<JavaSimplified_Expression> javasimplified_expressions;




    private JavaSimplified_MethodInvocation javasimplified_methodinvocation;




    private JavaSimplified_Name javasimplified_name;


    public JavaSimplified_MethodCall(
    ) {
        this.javasimplified_expressions = new ArrayList<>();
    }

    public JavaSimplified_MethodCall(
        ArrayList<JavaSimplified_Expression> javasimplified_expressions    ) {
        this.javasimplified_expressions = javasimplified_expressions;
    }


    public JavaSimplified_MethodCall getJavasimplified_methodcall() {
        return javasimplified_methodcall;
    }

    public void setJavasimplified_methodcall(JavaSimplified_MethodCall javasimplified_methodcall) {
        this.javasimplified_methodcall = javasimplified_methodcall;
    }
    public List<JavaSimplified_Expression> getJavasimplified_expressions() {
        return javasimplified_expressions;
    }

    public void addJavasimplified_expression(Javasimplified_expression javasimplified_expression) {
        this.javasimplified_expressions.add(javasimplified_expression);
    }
    public JavaSimplified_MethodInvocation getJavasimplified_methodinvocation() {
        return javasimplified_methodinvocation;
    }

    public void setJavasimplified_methodinvocation(JavaSimplified_MethodInvocation javasimplified_methodinvocation) {
        this.javasimplified_methodinvocation = javasimplified_methodinvocation;
    }
    public JavaSimplified_Name getJavasimplified_name() {
        return javasimplified_name;
    }

    public void setJavasimplified_name(JavaSimplified_Name javasimplified_name) {
        this.javasimplified_name = javasimplified_name;
    }

}