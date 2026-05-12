





import java.util.List;
import java.util.ArrayList;

public class WebADM  {

    private String state;
    private String password;
    private String login;





    private ShoppingCart shoppingcart;




    private Cliente cliente;


    public WebADM(
        String state,        String password,        String login    ) {
        this.state = state;
        this.password = password;
        this.login = login;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
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

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }
    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

}