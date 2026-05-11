





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppSwitchExpression extends CppExpression {






    private List<Metamodelo_Cpp_CppExpression> metamodelo_cpp_cppexpressions;




    private Metamodelo_Cpp_CppExpression metamodelo_cpp_cppexpression;




    private List<Metamodelo_Cpp_CppCase> metamodelo_cpp_cppcases;


    public Metamodelo_Cpp_CppSwitchExpression(
    ) {
        super(
        );
        this.metamodelo_cpp_cppexpressions = new ArrayList<>();
        this.metamodelo_cpp_cppcases = new ArrayList<>();
    }

    public Metamodelo_Cpp_CppSwitchExpression(
        ArrayList<Metamodelo_Cpp_CppExpression> metamodelo_cpp_cppexpressions,        ArrayList<Metamodelo_Cpp_CppCase> metamodelo_cpp_cppcases    ) {
        this.metamodelo_cpp_cppexpressions = metamodelo_cpp_cppexpressions;
        this.metamodelo_cpp_cppcases = metamodelo_cpp_cppcases;
    }


    public List<Metamodelo_Cpp_CppExpression> getMetamodelo_cpp_cppexpressions() {
        return metamodelo_cpp_cppexpressions;
    }

    public void addMetamodelo_cpp_cppexpression(Metamodelo_cpp_cppexpression metamodelo_cpp_cppexpression) {
        this.metamodelo_cpp_cppexpressions.add(metamodelo_cpp_cppexpression);
    }
    public Metamodelo_Cpp_CppExpression getMetamodelo_cpp_cppexpression() {
        return metamodelo_cpp_cppexpression;
    }

    public void setMetamodelo_cpp_cppexpression(Metamodelo_Cpp_CppExpression metamodelo_cpp_cppexpression) {
        this.metamodelo_cpp_cppexpression = metamodelo_cpp_cppexpression;
    }
    public List<Metamodelo_Cpp_CppCase> getMetamodelo_cpp_cppcases() {
        return metamodelo_cpp_cppcases;
    }

    public void addMetamodelo_cpp_cppcase(Metamodelo_cpp_cppcase metamodelo_cpp_cppcase) {
        this.metamodelo_cpp_cppcases.add(metamodelo_cpp_cppcase);
    }

}