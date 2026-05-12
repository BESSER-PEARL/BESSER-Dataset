





import java.util.List;
import java.util.ArrayList;

public class Funcion_rio  {

    private String Senha;
    private String Usuario;



    public Funcion_rio(
        String Senha,        String Usuario    ) {
        this.Senha = Senha;
        this.Usuario = Usuario;
    }


    public String getSenha() {
        return Senha;
    }

    public void setSenha(String Senha) {
        this.Senha = Senha;
    }
    public String getUsuario() {
        return Usuario;
    }

    public void setUsuario(String Usuario) {
        this.Usuario = Usuario;
    }


}