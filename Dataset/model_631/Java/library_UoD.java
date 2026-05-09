





import java.util.List;
import java.util.ArrayList;

public class library_UoD  {






    private List<library_Author> library_authors;




    private List<library_Person> library_persons;


    public library_UoD(
    ) {
        this.library_authors = new ArrayList<>();
        this.library_persons = new ArrayList<>();
    }

    public library_UoD(
        ArrayList<library_Author> library_authors,        ArrayList<library_Person> library_persons    ) {
        this.library_authors = library_authors;
        this.library_persons = library_persons;
    }


    public List<library_Author> getLibrary_authors() {
        return library_authors;
    }

    public void addLibrary_author(Library_author library_author) {
        this.library_authors.add(library_author);
    }
    public List<library_Person> getLibrary_persons() {
        return library_persons;
    }

    public void addLibrary_person(Library_person library_person) {
        this.library_persons.add(library_person);
    }

}