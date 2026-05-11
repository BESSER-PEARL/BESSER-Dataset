





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppTypeAccess extends CppExpression {






    private List<Metamodelo_Cpp_CppTypeAccess> metamodelo_cpp_cpptypeaccesss;




    private Metamodelo_Cpp_CppType metamodelo_cpp_cpptype;




    private Metamodelo_Cpp_CppType metamodelo_cpp_cpptype;




    private Metamodelo_Cpp_CppTypedElement metamodelo_cpp_cpptypedelement;


    public Metamodelo_Cpp_CppTypeAccess(
    ) {
        super(
        );
        this.metamodelo_cpp_cpptypeaccesss = new ArrayList<>();
    }

    public Metamodelo_Cpp_CppTypeAccess(
        ArrayList<Metamodelo_Cpp_CppTypeAccess> metamodelo_cpp_cpptypeaccesss    ) {
        this.metamodelo_cpp_cpptypeaccesss = metamodelo_cpp_cpptypeaccesss;
    }


    public List<Metamodelo_Cpp_CppTypeAccess> getMetamodelo_cpp_cpptypeaccesss() {
        return metamodelo_cpp_cpptypeaccesss;
    }

    public void addMetamodelo_cpp_cpptypeaccess(Metamodelo_cpp_cpptypeaccess metamodelo_cpp_cpptypeaccess) {
        this.metamodelo_cpp_cpptypeaccesss.add(metamodelo_cpp_cpptypeaccess);
    }
    public Metamodelo_Cpp_CppType getMetamodelo_cpp_cpptype() {
        return metamodelo_cpp_cpptype;
    }

    public void setMetamodelo_cpp_cpptype(Metamodelo_Cpp_CppType metamodelo_cpp_cpptype) {
        this.metamodelo_cpp_cpptype = metamodelo_cpp_cpptype;
    }
    public Metamodelo_Cpp_CppType getMetamodelo_cpp_cpptype() {
        return metamodelo_cpp_cpptype;
    }

    public void setMetamodelo_cpp_cpptype(Metamodelo_Cpp_CppType metamodelo_cpp_cpptype) {
        this.metamodelo_cpp_cpptype = metamodelo_cpp_cpptype;
    }
    public Metamodelo_Cpp_CppTypedElement getMetamodelo_cpp_cpptypedelement() {
        return metamodelo_cpp_cpptypedelement;
    }

    public void setMetamodelo_cpp_cpptypedelement(Metamodelo_Cpp_CppTypedElement metamodelo_cpp_cpptypedelement) {
        this.metamodelo_cpp_cpptypedelement = metamodelo_cpp_cpptypedelement;
    }

}