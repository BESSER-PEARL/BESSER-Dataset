





import java.util.List;
import java.util.ArrayList;

public class library_Author  {

    private String surname;
    private String first_name;



    public library_Author(
        String surname,        String first_name    ) {
        this.surname = surname;
        this.first_name = first_name;
    }


    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }
    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }


}