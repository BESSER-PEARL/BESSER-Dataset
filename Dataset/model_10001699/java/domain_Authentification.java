





import java.util.List;
import java.util.ArrayList;

public class domain_Authentification  {

    private String id;
    private String password;





    private List<domain_Profil> domain_profils;


    public domain_Authentification(
        String id,        String password    ) {
        this.id = id;
        this.password = password;
        this.domain_profils = new ArrayList<>();
    }

    public domain_Authentification(
        String id,        String password        ArrayList<domain_Profil> domain_profils    ) {
        this.id = id;
        this.password = password;
        this.domain_profils = domain_profils;
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

    public List<domain_Profil> getDomain_profils() {
        return domain_profils;
    }

    public void addDomain_profil(Domain_profil domain_profil) {
        this.domain_profils.add(domain_profil);
    }

}