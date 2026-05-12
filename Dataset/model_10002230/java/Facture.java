





import java.util.List;
import java.util.ArrayList;

public class Facture  {

    private boolean paye;
    private String numero;
    private int id_devis;



    public Facture(
        boolean paye,        String numero,        int id_devis    ) {
        this.paye = paye;
        this.numero = numero;
        this.id_devis = id_devis;
    }


    public boolean getPaye() {
        return paye;
    }

    public void setPaye(boolean paye) {
        this.paye = paye;
    }
    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }
    public int getId_devis() {
        return id_devis;
    }

    public void setId_devis(int id_devis) {
        this.id_devis = id_devis;
    }


}