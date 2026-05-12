





import java.util.List;
import java.util.ArrayList;

public class Laboratoire  {

    private String numero;
    private String nom;
    private int id;



    public Laboratoire(
        String numero,        String nom,        int id    ) {
        this.numero = numero;
        this.nom = nom;
        this.id = id;
    }


    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}