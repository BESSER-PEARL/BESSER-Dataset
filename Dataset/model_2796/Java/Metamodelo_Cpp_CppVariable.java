





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppVariable extends CppTypedElement, CppField, CppVariableDeclaration, CppType {

    private String storage;
    private boolean isConst;





    private Metamodelo_Cpp_CppClassifier metamodelo_cpp_cppclassifier;


    public Metamodelo_Cpp_CppVariable(
        String storage,        boolean isConst    ) {
        super(
        );
        this.storage = storage;
        this.isConst = isConst;
    }


    public String getStorage() {
        return storage;
    }

    public void setStorage(String storage) {
        this.storage = storage;
    }
    public boolean getIsconst() {
        return isConst;
    }

    public void setIsconst(boolean isConst) {
        this.isConst = isConst;
    }

    public Metamodelo_Cpp_CppClassifier getMetamodelo_cpp_cppclassifier() {
        return metamodelo_cpp_cppclassifier;
    }

    public void setMetamodelo_cpp_cppclassifier(Metamodelo_Cpp_CppClassifier metamodelo_cpp_cppclassifier) {
        this.metamodelo_cpp_cppclassifier = metamodelo_cpp_cppclassifier;
    }

}