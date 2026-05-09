





import java.util.List;
import java.util.ArrayList;

public class library_Author  {

    private String surname;
    private String name;



    public library_Author(
        String surname,        String name    ) {
        this.surname = surname;
        this.name = name;
    }


    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}