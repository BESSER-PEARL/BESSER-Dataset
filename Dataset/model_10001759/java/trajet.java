





import java.util.List;
import java.util.ArrayList;

public class trajet  {

    private float prix_du_trajet;
    private String la_date;
    private float l_heure_de_d_part;
    private String lieu_de_d_part;



    public trajet(
        float prix_du_trajet,        String la_date,        float l_heure_de_d_part,        String lieu_de_d_part    ) {
        this.prix_du_trajet = prix_du_trajet;
        this.la_date = la_date;
        this.l_heure_de_d_part = l_heure_de_d_part;
        this.lieu_de_d_part = lieu_de_d_part;
    }


    public float getPrix_du_trajet() {
        return prix_du_trajet;
    }

    public void setPrix_du_trajet(float prix_du_trajet) {
        this.prix_du_trajet = prix_du_trajet;
    }
    public String getLa_date() {
        return la_date;
    }

    public void setLa_date(String la_date) {
        this.la_date = la_date;
    }
    public float getL_heure_de_d_part() {
        return l_heure_de_d_part;
    }

    public void setL_heure_de_d_part(float l_heure_de_d_part) {
        this.l_heure_de_d_part = l_heure_de_d_part;
    }
    public String getLieu_de_d_part() {
        return lieu_de_d_part;
    }

    public void setLieu_de_d_part(String lieu_de_d_part) {
        this.lieu_de_d_part = lieu_de_d_part;
    }


}