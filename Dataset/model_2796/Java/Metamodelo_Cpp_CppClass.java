





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppClass extends CppClassifier {

    private String classkey;
    private boolean isFinal;
    private boolean isGeneric;
    private boolean isAbstract;





    private Metamodelo_Cpp_CppModel metamodelo_cpp_cppmodel;




    private Metamodelo_Cpp_CppClass metamodelo_cpp_cppclass;


    public Metamodelo_Cpp_CppClass(
        String classkey,        boolean isFinal,        boolean isGeneric,        boolean isAbstract    ) {
        super(
        );
        this.classkey = classkey;
        this.isFinal = isFinal;
        this.isGeneric = isGeneric;
        this.isAbstract = isAbstract;
    }


    public String getClasskey() {
        return classkey;
    }

    public void setClasskey(String classkey) {
        this.classkey = classkey;
    }
    public boolean getIsfinal() {
        return isFinal;
    }

    public void setIsfinal(boolean isFinal) {
        this.isFinal = isFinal;
    }
    public boolean getIsgeneric() {
        return isGeneric;
    }

    public void setIsgeneric(boolean isGeneric) {
        this.isGeneric = isGeneric;
    }
    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public Metamodelo_Cpp_CppModel getMetamodelo_cpp_cppmodel() {
        return metamodelo_cpp_cppmodel;
    }

    public void setMetamodelo_cpp_cppmodel(Metamodelo_Cpp_CppModel metamodelo_cpp_cppmodel) {
        this.metamodelo_cpp_cppmodel = metamodelo_cpp_cppmodel;
    }
    public Metamodelo_Cpp_CppClass getMetamodelo_cpp_cppclass() {
        return metamodelo_cpp_cppclass;
    }

    public void setMetamodelo_cpp_cppclass(Metamodelo_Cpp_CppClass metamodelo_cpp_cppclass) {
        this.metamodelo_cpp_cppclass = metamodelo_cpp_cppclass;
    }

}