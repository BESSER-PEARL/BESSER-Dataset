





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppVariableDeclarationGroup extends CppTypedElement {






    private List<Metamodelo_Cpp_CppVariableDeclarationFragment> metamodelo_cpp_cppvariabledeclarationfragments;




    private Metamodelo_Cpp_CppVariableDeclarationFragment metamodelo_cpp_cppvariabledeclarationfragment;


    public Metamodelo_Cpp_CppVariableDeclarationGroup(
    ) {
        super(
        );
        this.metamodelo_cpp_cppvariabledeclarationfragments = new ArrayList<>();
    }

    public Metamodelo_Cpp_CppVariableDeclarationGroup(
        ArrayList<Metamodelo_Cpp_CppVariableDeclarationFragment> metamodelo_cpp_cppvariabledeclarationfragments    ) {
        this.metamodelo_cpp_cppvariabledeclarationfragments = metamodelo_cpp_cppvariabledeclarationfragments;
    }


    public List<Metamodelo_Cpp_CppVariableDeclarationFragment> getMetamodelo_cpp_cppvariabledeclarationfragments() {
        return metamodelo_cpp_cppvariabledeclarationfragments;
    }

    public void addMetamodelo_cpp_cppvariabledeclarationfragment(Metamodelo_cpp_cppvariabledeclarationfragment metamodelo_cpp_cppvariabledeclarationfragment) {
        this.metamodelo_cpp_cppvariabledeclarationfragments.add(metamodelo_cpp_cppvariabledeclarationfragment);
    }
    public Metamodelo_Cpp_CppVariableDeclarationFragment getMetamodelo_cpp_cppvariabledeclarationfragment() {
        return metamodelo_cpp_cppvariabledeclarationfragment;
    }

    public void setMetamodelo_cpp_cppvariabledeclarationfragment(Metamodelo_Cpp_CppVariableDeclarationFragment metamodelo_cpp_cppvariabledeclarationfragment) {
        this.metamodelo_cpp_cppvariabledeclarationfragment = metamodelo_cpp_cppvariabledeclarationfragment;
    }

}