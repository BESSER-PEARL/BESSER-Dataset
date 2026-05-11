





import java.util.List;
import java.util.ArrayList;

public class picojava_Access extends Exp {






    private picojava_VarDecl picojava_vardecl;




    private picojava_TypeDecl picojava_typedecl;




    private picojava_Decl picojava_decl;


    public picojava_Access(
    ) {
        super(
        );
    }



    public picojava_VarDecl getPicojava_vardecl() {
        return picojava_vardecl;
    }

    public void setPicojava_vardecl(picojava_VarDecl picojava_vardecl) {
        this.picojava_vardecl = picojava_vardecl;
    }
    public picojava_TypeDecl getPicojava_typedecl() {
        return picojava_typedecl;
    }

    public void setPicojava_typedecl(picojava_TypeDecl picojava_typedecl) {
        this.picojava_typedecl = picojava_typedecl;
    }
    public picojava_Decl getPicojava_decl() {
        return picojava_decl;
    }

    public void setPicojava_decl(picojava_Decl picojava_decl) {
        this.picojava_decl = picojava_decl;
    }

}