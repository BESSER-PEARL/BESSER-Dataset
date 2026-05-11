





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppTypeParameter extends CppType {






    private Metamodelo_Cpp_CppType metamodelo_cpp_cpptype;




    private List<Metamodelo_Cpp_CppTypeAccess> metamodelo_cpp_cpptypeaccesss;


    public Metamodelo_Cpp_CppTypeParameter(
    ) {
        super(
        );
        this.metamodelo_cpp_cpptypeaccesss = new ArrayList<>();
    }

    public Metamodelo_Cpp_CppTypeParameter(
        ArrayList<Metamodelo_Cpp_CppTypeAccess> metamodelo_cpp_cpptypeaccesss    ) {
        this.metamodelo_cpp_cpptypeaccesss = metamodelo_cpp_cpptypeaccesss;
    }


    public Metamodelo_Cpp_CppType getMetamodelo_cpp_cpptype() {
        return metamodelo_cpp_cpptype;
    }

    public void setMetamodelo_cpp_cpptype(Metamodelo_Cpp_CppType metamodelo_cpp_cpptype) {
        this.metamodelo_cpp_cpptype = metamodelo_cpp_cpptype;
    }
    public List<Metamodelo_Cpp_CppTypeAccess> getMetamodelo_cpp_cpptypeaccesss() {
        return metamodelo_cpp_cpptypeaccesss;
    }

    public void addMetamodelo_cpp_cpptypeaccess(Metamodelo_cpp_cpptypeaccess metamodelo_cpp_cpptypeaccess) {
        this.metamodelo_cpp_cpptypeaccesss.add(metamodelo_cpp_cpptypeaccess);
    }

}