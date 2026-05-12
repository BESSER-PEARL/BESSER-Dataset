





import java.util.List;
import java.util.ArrayList;

public class Adresse  {

    private int code_postal;
    private String t_l_phone;
    private String voie;
    private String geocode;
    private int utilisateur_id;
    private int id;
    private String ville;
    private int num_ro;



    public Adresse(
        int code_postal,        String t_l_phone,        String voie,        String geocode,        int utilisateur_id,        int id,        String ville,        int num_ro    ) {
        this.code_postal = code_postal;
        this.t_l_phone = t_l_phone;
        this.voie = voie;
        this.geocode = geocode;
        this.utilisateur_id = utilisateur_id;
        this.id = id;
        this.ville = ville;
        this.num_ro = num_ro;
    }


    public int getCode_postal() {
        return code_postal;
    }

    public void setCode_postal(int code_postal) {
        this.code_postal = code_postal;
    }
    public String getT_l_phone() {
        return t_l_phone;
    }

    public void setT_l_phone(String t_l_phone) {
        this.t_l_phone = t_l_phone;
    }
    public String getVoie() {
        return voie;
    }

    public void setVoie(String voie) {
        this.voie = voie;
    }
    public String getGeocode() {
        return geocode;
    }

    public void setGeocode(String geocode) {
        this.geocode = geocode;
    }
    public int getUtilisateur_id() {
        return utilisateur_id;
    }

    public void setUtilisateur_id(int utilisateur_id) {
        this.utilisateur_id = utilisateur_id;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getVille() {
        return ville;
    }

    public void setVille(String ville) {
        this.ville = ville;
    }
    public int getNum_ro() {
        return num_ro;
    }

    public void setNum_ro(int num_ro) {
        this.num_ro = num_ro;
    }


}