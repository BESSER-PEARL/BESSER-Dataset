





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppBlock extends CppExpression {






    private List<Metamodelo_Cpp_CppExpression> metamodelo_cpp_cppexpressions;




    private Metamodelo_Cpp_CppFunction metamodelo_cpp_cppfunction;


    public Metamodelo_Cpp_CppBlock(
    ) {
        super(
        );
        this.metamodelo_cpp_cppexpressions = new ArrayList<>();
    }

    public Metamodelo_Cpp_CppBlock(
        ArrayList<Metamodelo_Cpp_CppExpression> metamodelo_cpp_cppexpressions    ) {
        this.metamodelo_cpp_cppexpressions = metamodelo_cpp_cppexpressions;
    }


    public List<Metamodelo_Cpp_CppExpression> getMetamodelo_cpp_cppexpressions() {
        return metamodelo_cpp_cppexpressions;
    }

    public void addMetamodelo_cpp_cppexpression(Metamodelo_cpp_cppexpression metamodelo_cpp_cppexpression) {
        this.metamodelo_cpp_cppexpressions.add(metamodelo_cpp_cppexpression);
    }
    public Metamodelo_Cpp_CppFunction getMetamodelo_cpp_cppfunction() {
        return metamodelo_cpp_cppfunction;
    }

    public void setMetamodelo_cpp_cppfunction(Metamodelo_Cpp_CppFunction metamodelo_cpp_cppfunction) {
        this.metamodelo_cpp_cppfunction = metamodelo_cpp_cppfunction;
    }

}