





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String password;
    private String login;
    private String state;





    private Venta venta;




    private Vendedor vendedor;


    public Login(
        String password,        String login,        String state    ) {
        this.password = password;
        this.login = login;
        this.state = state;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public Venta getVenta() {
        return venta;
    }

    public void setVenta(Venta venta) {
        this.venta = venta;
    }
    public Vendedor getVendedor() {
        return vendedor;
    }

    public void setVendedor(Vendedor vendedor) {
        this.vendedor = vendedor;
    }

}