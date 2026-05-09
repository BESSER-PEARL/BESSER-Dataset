




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_Writer  {

    private String lastName;
    private String firstName;
    private LocalDate BirthDate;
    private boolean Pseudonym;
    private String EMail;





    private model_Library model_library;




    private model_Library model_library;


    public model_Writer(
        String lastName,        String firstName,        LocalDate BirthDate,        boolean Pseudonym,        String EMail    ) {
        this.lastName = lastName;
        this.firstName = firstName;
        this.BirthDate = BirthDate;
        this.Pseudonym = Pseudonym;
        this.EMail = EMail;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public LocalDate getBirthdate() {
        return BirthDate;
    }

    public void setBirthdate(LocalDate BirthDate) {
        this.BirthDate = BirthDate;
    }
    public boolean getPseudonym() {
        return Pseudonym;
    }

    public void setPseudonym(boolean Pseudonym) {
        this.Pseudonym = Pseudonym;
    }
    public String getEmail() {
        return EMail;
    }

    public void setEmail(String EMail) {
        this.EMail = EMail;
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