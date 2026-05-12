





import java.util.List;
import java.util.ArrayList;

public class R_le  {

    private int id;
    private String type;





    private List<Utilisateur> utilisateurs;


    public R_le(
        int id,        String type    ) {
        this.id = id;
        this.type = type;
        this.utilisateurs = new ArrayList<>();
    }

    public R_le(
        int id,        String type        ArrayList<Utilisateur> utilisateurs    ) {
        this.id = id;
        this.type = type;
        this.utilisateurs = utilisateurs;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<Utilisateur> getUtilisateurs() {
        return utilisateurs;
    }

    public void addUtilisateur(Utilisateur utilisateur) {
        this.utilisateurs.add(utilisateur);
    }

}