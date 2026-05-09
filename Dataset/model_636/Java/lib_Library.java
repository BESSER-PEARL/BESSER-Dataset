





import java.util.List;
import java.util.ArrayList;

public class lib_Library  {

    private String name;





    private List<lib_Person> lib_persons;




    private lib_Cafeteria lib_cafeteria;




    private lib_Cafeteria lib_cafeteria;




    private lib_Person lib_person;


    public lib_Library(
        String name    ) {
        this.name = name;
        this.lib_persons = new ArrayList<>();
    }

    public lib_Library(
        String name        ArrayList<lib_Person> lib_persons    ) {
        this.name = name;
        this.lib_persons = lib_persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<lib_Person> getLib_persons() {
        return lib_persons;
    }

    public void addLib_person(Lib_person lib_person) {
        this.lib_persons.add(lib_person);
    }
    public lib_Cafeteria getLib_cafeteria() {
        return lib_cafeteria;
    }

    public void setLib_cafeteria(lib_Cafeteria lib_cafeteria) {
        this.lib_cafeteria = lib_cafeteria;
    }
    public lib_Cafeteria getLib_cafeteria() {
        return lib_cafeteria;
    }

    public void setLib_cafeteria(lib_Cafeteria lib_cafeteria) {
        this.lib_cafeteria = lib_cafeteria;
    }
    public lib_Person getLib_person() {
        return lib_person;
    }

    public void setLib_person(lib_Person lib_person) {
        this.lib_person = lib_person;
    }

}