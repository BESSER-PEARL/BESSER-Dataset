





import java.util.List;
import java.util.ArrayList;

public class AuthenticationService  {

    private String attribute3;
    private String attribute2;
    private String attribute4;
    private String user;
    private String authState;
    private String attribute;
    private None role;





    private AuthenticationService authenticationservice;




    private Usuario_Interface usuario_interface;


    public AuthenticationService(
        String attribute3,        String attribute2,        String attribute4,        String user,        String authState,        String attribute,        None role    ) {
        this.attribute3 = attribute3;
        this.attribute2 = attribute2;
        this.attribute4 = attribute4;
        this.user = user;
        this.authState = authState;
        this.attribute = attribute;
        this.role = role;
    }


    public String getAttribute3() {
        return attribute3;
    }

    public void setAttribute3(String attribute3) {
        this.attribute3 = attribute3;
    }
    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }
    public String getAttribute4() {
        return attribute4;
    }

    public void setAttribute4(String attribute4) {
        this.attribute4 = attribute4;
    }
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }
    public String getAuthstate() {
        return authState;
    }

    public void setAuthstate(String authState) {
        this.authState = authState;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public None getRole() {
        return role;
    }

    public void setRole(None role) {
        this.role = role;
    }

    public AuthenticationService getAuthenticationservice() {
        return authenticationservice;
    }

    public void setAuthenticationservice(AuthenticationService authenticationservice) {
        this.authenticationservice = authenticationservice;
    }
    public Usuario_Interface getUsuario_interface() {
        return usuario_interface;
    }

    public void setUsuario_interface(Usuario_Interface usuario_interface) {
        this.usuario_interface = usuario_interface;
    }

}