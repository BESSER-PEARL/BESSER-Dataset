





import java.util.List;
import java.util.ArrayList;

public class gedcoml_Author  {

    private String firstName;
    private String lastName;





    private gedcoml_Projectdescription gedcoml_projectdescription;


    public gedcoml_Author(
        String firstName,        String lastName    ) {
        this.firstName = firstName;
        this.lastName = lastName;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }

    public gedcoml_Projectdescription getGedcoml_projectdescription() {
        return gedcoml_projectdescription;
    }

    public void setGedcoml_projectdescription(gedcoml_Projectdescription gedcoml_projectdescription) {
        this.gedcoml_projectdescription = gedcoml_projectdescription;
    }

}