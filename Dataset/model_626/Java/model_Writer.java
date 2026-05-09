




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_Writer  {

    private boolean Pseudonym;
    private LocalDate BirthDate;
    private String lastName;
    private String EMail;
    private String firstName;





    private model_Library model_library;




    private model_Library model_library;


    public model_Writer(
        boolean Pseudonym,        LocalDate BirthDate,        String lastName,        String EMail,        String firstName    ) {
        this.Pseudonym = Pseudonym;
        this.BirthDate = BirthDate;
        this.lastName = lastName;
        this.EMail = EMail;
        this.firstName = firstName;
    }


    public boolean getPseudonym() {
        return Pseudonym;
    }

    public void setPseudonym(boolean Pseudonym) {
        this.Pseudonym = Pseudonym;
    }
    public LocalDate getBirthdate() {
        return BirthDate;
    }

    public void setBirthdate(LocalDate BirthDate) {
        this.BirthDate = BirthDate;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getEmail() {
        return EMail;
    }

    public void setEmail(String EMail) {
        this.EMail = EMail;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public model_Library getModel_library() {
        return model_library;
    }

    public void setModel_library(model_Library model_library) {
        this.model_library = model_library;
    }
    public model_Library getModel_library() {
        return model_library;
    }

    public void setModel_library(model_Library model_library) {
        this.model_library = model_library;
    }

}