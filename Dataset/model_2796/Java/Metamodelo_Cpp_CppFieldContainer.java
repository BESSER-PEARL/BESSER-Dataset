





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppFieldContainer extends CppModelElement {






    private Metamodelo_Cpp_CppField metamodelo_cpp_cppfield;




    private List<Metamodelo_Cpp_CppField> metamodelo_cpp_cppfields;


    public Metamodelo_Cpp_CppFieldContainer(
    ) {
        super(
        );
        this.metamodelo_cpp_cppfields = new ArrayList<>();
    }

    public Metamodelo_Cpp_CppFieldContainer(
        ArrayList<Metamodelo_Cpp_CppField> metamodelo_cpp_cppfields    ) {
        this.metamodelo_cpp_cppfields = metamodelo_cpp_cppfields;
    }


    public Metamodelo_Cpp_CppField getMetamodelo_cpp_cppfield() {
        return metamodelo_cpp_cppfield;
    }

    public void setMetamodelo_cpp_cppfield(Metamodelo_Cpp_CppField metamodelo_cpp_cppfield) {
        this.metamodelo_cpp_cppfield = metamodelo_cpp_cppfield;
    }
    public List<Metamodelo_Cpp_CppField> getMetamodelo_cpp_cppfields() {
        return metamodelo_cpp_cppfields;
    }

    public void addMetamodelo_cpp_cppfield(Metamodelo_cpp_cppfield metamodelo_cpp_cppfield) {
        this.metamodelo_cpp_cppfields.add(metamodelo_cpp_cppfield);
    }

}