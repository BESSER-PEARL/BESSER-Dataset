





import java.util.List;
import java.util.ArrayList;

public class sistedesMM_Person  {

    private String name;
    private String nationality;
    private String surname;
    private String email;



    public sistedesMM_Person(
        String name,        String nationality,        String surname,        String email    ) {
        this.name = name;
        this.nationality = nationality;
        this.surname = surname;
        this.email = email;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNationality() {
        return nationality;
    }

    public void setNationality(String nationality) {
        this.nationality = nationality;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}