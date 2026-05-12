





import java.util.List;
import java.util.ArrayList;

public class Covoiturage_Authentification  {

    private String id;
    private String password;





    private List<Covoiturage_Passager> covoiturage_passagers;


    public Covoiturage_Authentification(
        String id,        String password    ) {
        this.id = id;
        this.password = password;
        this.covoiturage_passagers = new ArrayList<>();
    }

    public Covoiturage_Authentification(
        String id,        String password        ArrayList<Covoiturage_Passager> covoiturage_passagers    ) {
        this.id = id;
        this.password = password;
        this.covoiturage_passagers = covoiturage_passagers;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public List<Covoiturage_Passager> getCovoiturage_passagers() {
        return covoiturage_passagers;
    }

    public void addCovoiturage_passager(Covoiturage_passager covoiturage_passager) {
        this.covoiturage_passagers.add(covoiturage_passager);
    }

}