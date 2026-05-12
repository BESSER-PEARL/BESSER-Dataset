





import java.util.List;
import java.util.ArrayList;

public class DevisEntete  {

    private String numero;
    private int id_session;



    public DevisEntete(
        String numero,        int id_session    ) {
        this.numero = numero;
        this.id_session = id_session;
    }


    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }
    public int getId_session() {
        return id_session;
    }

    public void setId_session(int id_session) {
        this.id_session = id_session;
    }


}