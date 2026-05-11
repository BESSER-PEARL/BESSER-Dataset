





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppTryExpression extends CppExpression {






    private List<Metamodelo_Cpp_CppCatchClause> metamodelo_cpp_cppcatchclauses;




    private Metamodelo_Cpp_CppExpression metamodelo_cpp_cppexpression;


    public Metamodelo_Cpp_CppTryExpression(
    ) {
        super(
        );
        this.metamodelo_cpp_cppcatchclauses = new ArrayList<>();
    }

    public Metamodelo_Cpp_CppTryExpression(
        ArrayList<Metamodelo_Cpp_CppCatchClause> metamodelo_cpp_cppcatchclauses    ) {
        this.metamodelo_cpp_cppcatchclauses = metamodelo_cpp_cppcatchclauses;
    }


    public List<Metamodelo_Cpp_CppCatchClause> getMetamodelo_cpp_cppcatchclauses() {
        return metamodelo_cpp_cppcatchclauses;
    }

    public void addMetamodelo_cpp_cppcatchclause(Metamodelo_cpp_cppcatchclause metamodelo_cpp_cppcatchclause) {
        this.metamodelo_cpp_cppcatchclauses.add(metamodelo_cpp_cppcatchclause);
    }
    public Metamodelo_Cpp_CppExpression getMetamodelo_cpp_cppexpression() {
        return metamodelo_cpp_cppexpression;
    }

    public void setMetamodelo_cpp_cppexpression(Metamodelo_Cpp_CppExpression metamodelo_cpp_cppexpression) {
        this.metamodelo_cpp_cppexpression = metamodelo_cpp_cppexpression;
    }

}