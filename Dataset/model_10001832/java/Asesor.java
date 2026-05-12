





import java.util.List;
import java.util.ArrayList;

public class Asesor  {

    private String pass;
    private String user;
    private int id;





    private Cliente cliente;


    public Asesor(
        String pass,        String user,        int id    ) {
        this.pass = pass;
        this.user = user;
        this.id = id;
    }


    public String getPass() {
        return pass;
    }

    public void setPass(String pass) {
        this.pass = pass;
    }
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

}