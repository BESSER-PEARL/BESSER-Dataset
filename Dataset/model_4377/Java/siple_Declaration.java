





import java.util.List;
import java.util.ArrayList;

public class siple_Declaration extends Statement {

    private String Type;
    private String Name;
    private boolean IsParameterDeclaration;





    private siple_CompilationUnit siple_compilationunit;


    public siple_Declaration(
        String Type,        String Name,        boolean IsParameterDeclaration    ) {
        super(
        );
        this.Type = Type;
        this.Name = Name;
        this.IsParameterDeclaration = IsParameterDeclaration;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public boolean getIsparameterdeclaration() {
        return IsParameterDeclaration;
    }

    public void setIsparameterdeclaration(boolean IsParameterDeclaration) {
        this.IsParameterDeclaration = IsParameterDeclaration;
    }

    public siple_CompilationUnit getSiple_compilationunit() {
        return siple_compilationunit;
    }

    public void setSiple_compilationunit(siple_CompilationUnit siple_compilationunit) {
        this.siple_compilationunit = siple_compilationunit;
    }

}