





import java.util.List;
import java.util.ArrayList;

public class Gerente  {

    private String user;
    private String pass;
    private int id;





    private Sucursal sucursal;




    private Cliente cliente;


    public Gerente(
        String user,        String pass,        int id    ) {
        this.user = user;
        this.pass = pass;
        this.id = id;
    }


    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }
    public String getPass() {
        return pass;
    }

    public void setPass(String pass) {
        this.pass = pass;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Sucursal getSucursal() {
        return sucursal;
    }

    public void setSucursal(Sucursal sucursal) {
        this.sucursal = sucursal;
    }
    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

}