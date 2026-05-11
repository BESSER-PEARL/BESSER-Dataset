





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppDeclarationExpression extends CppExpression {






    private Metamodelo_Cpp_CppVariableDeclarationGroup metamodelo_cpp_cppvariabledeclarationgroup;




    private List<Metamodelo_Cpp_CppVariableDeclarationGroup> metamodelo_cpp_cppvariabledeclarationgroups;


    public Metamodelo_Cpp_CppDeclarationExpression(
    ) {
        super(
        );
        this.metamodelo_cpp_cppvariabledeclarationgroups = new ArrayList<>();
    }

    public Metamodelo_Cpp_CppDeclarationExpression(
        ArrayList<Metamodelo_Cpp_CppVariableDeclarationGroup> metamodelo_cpp_cppvariabledeclarationgroups    ) {
        this.metamodelo_cpp_cppvariabledeclarationgroups = metamodelo_cpp_cppvariabledeclarationgroups;
    }


    public Metamodelo_Cpp_CppVariableDeclarationGroup getMetamodelo_cpp_cppvariabledeclarationgroup() {
        return metamodelo_cpp_cppvariabledeclarationgroup;
    }

    public void setMetamodelo_cpp_cppvariabledeclarationgroup(Metamodelo_Cpp_CppVariableDeclarationGroup metamodelo_cpp_cppvariabledeclarationgroup) {
        this.metamodelo_cpp_cppvariabledeclarationgroup = metamodelo_cpp_cppvariabledeclarationgroup;
    }
    public List<Metamodelo_Cpp_CppVariableDeclarationGroup> getMetamodelo_cpp_cppvariabledeclarationgroups() {
        return metamodelo_cpp_cppvariabledeclarationgroups;
    }

    public void addMetamodelo_cpp_cppvariabledeclarationgroup(Metamodelo_cpp_cppvariabledeclarationgroup metamodelo_cpp_cppvariabledeclarationgroup) {
        this.metamodelo_cpp_cppvariabledeclarationgroups.add(metamodelo_cpp_cppvariabledeclarationgroup);
    }

}