





import java.util.List;
import java.util.ArrayList;

public class library_VideoCassette extends AudioVisualItem {






    private List<library_Person> library_persons;


    public library_VideoCassette(
    ) {
        super(
        );
        this.library_persons = new ArrayList<>();
    }

    public library_VideoCassette(
        ArrayList<library_Person> library_persons    ) {
        this.library_persons = library_persons;
    }


    public List<library_Person> getLibrary_persons() {
        return library_persons;
    }

    public void addLibrary_person(Library_person library_person) {
        this.library_persons.add(library_person);
    }

}