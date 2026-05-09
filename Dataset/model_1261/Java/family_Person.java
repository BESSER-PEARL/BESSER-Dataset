





import java.util.List;
import java.util.ArrayList;

public class family_Person  {

    private String firstName;
    private String sexe;



    public family_Person(
        String firstName,        String sexe    ) {
        this.firstName = firstName;
        this.sexe = sexe;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getSexe() {
        return sexe;
    }

    public void setSexe(String sexe) {
        this.sexe = sexe;
    }


}