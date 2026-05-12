





import java.util.List;
import java.util.ArrayList;

public class Funcionario  {

    private String Login;
    private int Id;
    private String Senha;
    private int Perfil;
    private String Nome;



    public Funcionario(
        String Login,        int Id,        String Senha,        int Perfil,        String Nome    ) {
        this.Login = Login;
        this.Id = Id;
        this.Senha = Senha;
        this.Perfil = Perfil;
        this.Nome = Nome;
    }


    public String getLogin() {
        return Login;
    }

    public void setLogin(String Login) {
        this.Login = Login;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public String getSenha() {
        return Senha;
    }

    public void setSenha(String Senha) {
        this.Senha = Senha;
    }
    public int getPerfil() {
        return Perfil;
    }

    public void setPerfil(int Perfil) {
        this.Perfil = Perfil;
    }
    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }


}