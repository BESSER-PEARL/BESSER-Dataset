





import java.util.List;
import java.util.ArrayList;

public class Laboratoire  {

    private String numero;
    private int id;
    private String nom;



    public Laboratoire(
        String numero,        int id,        String nom    ) {
        this.numero = numero;
        this.id = id;
        this.nom = nom;
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
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }


}