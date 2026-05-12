





import java.util.List;
import java.util.ArrayList;

public class Contact  {

    private int telephone;
    private String mail;
    private int id;





    private Personne personne;


    public Contact(
        int telephone,        String mail,        int id    ) {
        this.telephone = telephone;
        this.mail = mail;
        this.id = id;
    }


    public int getTelephone() {
        return telephone;
    }

    public void setTelephone(int telephone) {
        this.telephone = telephone;
    }
    public String getMail() {
        return mail;
    }

    public void setMail(String mail) {
        this.mail = mail;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Personne getPersonne() {
        return personne;
    }

    public void setPersonne(Personne personne) {
        this.personne = personne;
    }

}