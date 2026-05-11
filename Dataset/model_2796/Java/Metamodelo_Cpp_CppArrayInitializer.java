





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppArrayInitializer extends CppExpression {






    private List<Metamodelo_Cpp_CppExpression> metamodelo_cpp_cppexpressions;


    public Metamodelo_Cpp_CppArrayInitializer(
    ) {
        super(
        );
        this.metamodelo_cpp_cppexpressions = new ArrayList<>();
    }

    public Metamodelo_Cpp_CppArrayInitializer(
        ArrayList<Metamodelo_Cpp_CppExpression> metamodelo_cpp_cppexpressions    ) {
        this.metamodelo_cpp_cppexpressions = metamodelo_cpp_cppexpressions;
    }


    public List<Metamodelo_Cpp_CppExpression> getMetamodelo_cpp_cppexpressions() {
        return metamodelo_cpp_cppexpressions;
    }

    public void addMetamodelo_cpp_cppexpression(Metamodelo_cpp_cppexpression metamodelo_cpp_cppexpression) {
        this.metamodelo_cpp_cppexpressions.add(metamodelo_cpp_cppexpression);
    }

}