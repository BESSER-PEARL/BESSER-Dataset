





import java.util.List;
import java.util.ArrayList;

public class Delivering_Management  {

    private String deliver_boy_id;
    private String client_key;
    private String client_name;





    private Gestion_de_Limpieza gestion_de_limpieza;




    private Usuario usuario;


    public Delivering_Management(
        String deliver_boy_id,        String client_key,        String client_name    ) {
        this.deliver_boy_id = deliver_boy_id;
        this.client_key = client_key;
        this.client_name = client_name;
    }


    public String getDeliver_boy_id() {
        return deliver_boy_id;
    }

    public void setDeliver_boy_id(String deliver_boy_id) {
        this.deliver_boy_id = deliver_boy_id;
    }
    public String getClient_key() {
        return client_key;
    }

    public void setClient_key(String client_key) {
        this.client_key = client_key;
    }
    public String getClient_name() {
        return client_name;
    }

    public void setClient_name(String client_name) {
        this.client_name = client_name;
    }

    public Gestion_de_Limpieza getGestion_de_limpieza() {
        return gestion_de_limpieza;
    }

    public void setGestion_de_limpieza(Gestion_de_Limpieza gestion_de_limpieza) {
        this.gestion_de_limpieza = gestion_de_limpieza;
    }
    public Usuario getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }

}