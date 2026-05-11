





import java.util.List;
import java.util.ArrayList;

public class go_FunctionType  {

    private String nome;





    private go_Signature go_signature;




    private go_BLOCK go_block;




    private go_GoDecl go_godecl;


    public go_FunctionType(
        String nome    ) {
        this.nome = nome;
    }


    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public go_Signature getGo_signature() {
        return go_signature;
    }

    public void setGo_signature(go_Signature go_signature) {
        this.go_signature = go_signature;
    }
    public go_BLOCK getGo_block() {
        return go_block;
    }

    public void setGo_block(go_BLOCK go_block) {
        this.go_block = go_block;
    }
    public go_GoDecl getGo_godecl() {
        return go_godecl;
    }

    public void setGo_godecl(go_GoDecl go_godecl) {
        this.go_godecl = go_godecl;
    }

}