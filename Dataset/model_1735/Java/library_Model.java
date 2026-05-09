





import java.util.List;
import java.util.ArrayList;

public class library_Model  {






    private List<library_Library> library_librarys;




    private List<library_Person> library_persons;


    public library_Model(
    ) {
        this.library_librarys = new ArrayList<>();
        this.library_persons = new ArrayList<>();
    }

    public library_Model(
        ArrayList<library_Library> library_librarys,        ArrayList<library_Person> library_persons    ) {
        this.library_librarys = library_librarys;
        this.library_persons = library_persons;
    }


    public List<library_Library> getLibrary_librarys() {
        return library_librarys;
    }

    public void addLibrary_library(Library_library library_library) {
        this.library_librarys.add(library_library);
    }
    public List<library_Person> getLibrary_persons() {
        return library_persons;
    }

    public void addLibrary_person(Library_person library_person) {
        this.library_persons.add(library_person);
    }

}