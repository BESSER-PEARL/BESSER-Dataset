





import java.util.List;
import java.util.ArrayList;

public class Contact  {

    private int id;
    private int telephone;
    private String mail;





    private Personne personne;


    public Contact(
        int id,        int telephone,        String mail    ) {
        this.id = id;
        this.telephone = telephone;
        this.mail = mail;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
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

    public Personne getPersonne() {
        return personne;
    }

    public void setPersonne(Personne personne) {
        this.personne = personne;
    }

}