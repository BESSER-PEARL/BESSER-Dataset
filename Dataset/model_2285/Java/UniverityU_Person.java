





import java.util.List;
import java.util.ArrayList;

public class UniverityU_Person extends uncertainty_aPerson, uncertainty_ModelElement {

    private String Email;
    private String Name;



    public UniverityU_Person(
        String Email,        String Name    ) {
        super(
        );
        this.Email = Email;
        this.Name = Name;
    }


    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}