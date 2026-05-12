





import java.util.List;
import java.util.ArrayList;

public class Login1  {

    private String password;
    private String usuario;



    public Login1(
        String password,        String usuario    ) {
        this.password = password;
        this.usuario = usuario;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUsuario() {
        return usuario;
    }

    public void setUsuario(String usuario) {
        this.usuario = usuario;
    }


}