





import java.util.List;
import java.util.ArrayList;

public class Compte  {

    private String login;
    private String password;
    private String typeCompte;





    private Employe employe;




    private Patient patient;


    public Compte(
        String login,        String password,        String typeCompte    ) {
        this.login = login;
        this.password = password;
        this.typeCompte = typeCompte;
    }


    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getTypecompte() {
        return typeCompte;
    }

    public void setTypecompte(String typeCompte) {
        this.typeCompte = typeCompte;
    }

    public Employe getEmploye() {
        return employe;
    }

    public void setEmploye(Employe employe) {
        this.employe = employe;
    }
    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}