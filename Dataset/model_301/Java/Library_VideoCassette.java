





import java.util.List;
import java.util.ArrayList;

public class Library_VideoCassette extends AudioVisualItem {






    private List<Library_Person> library_persons;


    public Library_VideoCassette(
    ) {
        super(
        );
        this.library_persons = new ArrayList<>();
    }

    public Library_VideoCassette(
        ArrayList<Library_Person> library_persons    ) {
        this.library_persons = library_persons;
    }


    public List<Library_Person> getLibrary_persons() {
        return library_persons;
    }

    public void addLibrary_person(Library_person library_person) {
        this.library_persons.add(library_person);
    }

}