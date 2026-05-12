





import java.util.List;
import java.util.ArrayList;

public class Rendez_vous  {

    private int id;
    private String numero;
    private String date;



    public Rendez_vous(
        int id,        String numero,        String date    ) {
        this.id = id;
        this.numero = numero;
        this.date = date;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }


}