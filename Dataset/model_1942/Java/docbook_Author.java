





import java.util.List;
import java.util.ArrayList;

public class docbook_Author  {

    private String honorific;
    private String authorblug;
    private String firstname;
    private String surname;



    public docbook_Author(
        String honorific,        String authorblug,        String firstname,        String surname    ) {
        this.honorific = honorific;
        this.authorblug = authorblug;
        this.firstname = firstname;
        this.surname = surname;
    }


    public String getHonorific() {
        return honorific;
    }

    public void setHonorific(String honorific) {
        this.honorific = honorific;
    }
    public String getAuthorblug() {
        return authorblug;
    }

    public void setAuthorblug(String authorblug) {
        this.authorblug = authorblug;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }


}