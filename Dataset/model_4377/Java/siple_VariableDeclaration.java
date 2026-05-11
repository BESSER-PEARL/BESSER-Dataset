





import java.util.List;
import java.util.ArrayList;

public class siple_VariableDeclaration extends Declaration {

    private String DeclaredType;





    private siple_ProcedureDeclaration siple_proceduredeclaration;


    public siple_VariableDeclaration(
        String DeclaredType    ) {
        super(
        );
        this.DeclaredType = DeclaredType;
    }


    public String getDeclaredtype() {
        return DeclaredType;
    }

    public void setDeclaredtype(String DeclaredType) {
        this.DeclaredType = DeclaredType;
    }

    public siple_ProcedureDeclaration getSiple_proceduredeclaration() {
        return siple_proceduredeclaration;
    }

    public void setSiple_proceduredeclaration(siple_ProcedureDeclaration siple_proceduredeclaration) {
        this.siple_proceduredeclaration = siple_proceduredeclaration;
    }

}