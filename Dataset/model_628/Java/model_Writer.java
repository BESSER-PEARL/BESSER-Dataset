




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_Writer  {

    private String initials;
    private boolean Pseudonym;
    private String firstName;
    private String title;
    private LocalDate BirthDate;
    private String EMail;
    private String lastName;





    private model_Library model_library;




    private model_Library model_library;


    public model_Writer(
        String initials,        boolean Pseudonym,        String firstName,        String title,        LocalDate BirthDate,        String EMail,        String lastName    ) {
        this.initials = initials;
        this.Pseudonym = Pseudonym;
        this.firstName = firstName;
        this.title = title;
        this.BirthDate = BirthDate;
        this.EMail = EMail;
        this.lastName = lastName;
    }


    public String getInitials() {
        return initials;
    }

    public void setInitials(String initials) {
        this.initials = initials;
    }
    public boolean getPseudonym() {
        return Pseudonym;
    }

    public void setPseudonym(boolean Pseudonym) {
        this.Pseudonym = Pseudonym;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public LocalDate getBirthdate() {
        return BirthDate;
    }

    public void setBirthdate(LocalDate BirthDate) {
        this.BirthDate = BirthDate;
    }
    public String getEmail() {
        return EMail;
    }

    public void setEmail(String EMail) {
        this.EMail = EMail;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
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