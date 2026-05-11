





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppAbstractMethodInvocation extends CppExpression {






    private List<Metamodelo_Cpp_CppExpression> metamodelo_cpp_cppexpressions;




    private Metamodelo_Cpp_CppMemberFunction metamodelo_cpp_cppmemberfunction;


    public Metamodelo_Cpp_CppAbstractMethodInvocation(
    ) {
        super(
        );
        this.metamodelo_cpp_cppexpressions = new ArrayList<>();
    }

    public Metamodelo_Cpp_CppAbstractMethodInvocation(
        ArrayList<Metamodelo_Cpp_CppExpression> metamodelo_cpp_cppexpressions    ) {
        this.metamodelo_cpp_cppexpressions = metamodelo_cpp_cppexpressions;
    }


    public List<Metamodelo_Cpp_CppExpression> getMetamodelo_cpp_cppexpressions() {
        return metamodelo_cpp_cppexpressions;
    }

    public void addMetamodelo_cpp_cppexpression(Metamodelo_cpp_cppexpression metamodelo_cpp_cppexpression) {
        this.metamodelo_cpp_cppexpressions.add(metamodelo_cpp_cppexpression);
    }
    public Metamodelo_Cpp_CppMemberFunction getMetamodelo_cpp_cppmemberfunction() {
        return metamodelo_cpp_cppmemberfunction;
    }

    public void setMetamodelo_cpp_cppmemberfunction(Metamodelo_Cpp_CppMemberFunction metamodelo_cpp_cppmemberfunction) {
        this.metamodelo_cpp_cppmemberfunction = metamodelo_cpp_cppmemberfunction;
    }

}