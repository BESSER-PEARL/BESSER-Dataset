





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppFunction extends CppModelElement, CppType {

    private boolean isVarArg;
    private String linkage;
    private boolean isInline;



    public Metamodelo_Cpp_CppFunction(
        boolean isVarArg,        String linkage,        boolean isInline    ) {
        super(
        );
        this.isVarArg = isVarArg;
        this.linkage = linkage;
        this.isInline = isInline;
    }


    public boolean getIsvararg() {
        return isVarArg;
    }

    public void setIsvararg(boolean isVarArg) {
        this.isVarArg = isVarArg;
    }
    public String getLinkage() {
        return linkage;
    }

    public void setLinkage(String linkage) {
        this.linkage = linkage;
    }
    public boolean getIsinline() {
        return isInline;
    }

    public void setIsinline(boolean isInline) {
        this.isInline = isInline;
    }


}