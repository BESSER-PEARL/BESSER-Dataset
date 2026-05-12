





import java.util.List;
import java.util.ArrayList;

public class Rendez_vous  {

    private String numero;
    private int id;
    private String date;



    public Rendez_vous(
        String numero,        int id,        String date    ) {
        this.numero = numero;
        this.id = id;
        this.date = date;
    }


    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }


}