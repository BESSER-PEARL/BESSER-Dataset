





import java.util.List;
import java.util.ArrayList;

public class library_Author  {

    private String name;
    private String surname;



    public library_Author(
        String name,        String surname    ) {
        this.name = name;
        this.surname = surname;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }


}