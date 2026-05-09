





import java.util.List;
import java.util.ArrayList;

public class extlibrary_VideoCassette extends AudioVisualItem {






    private List<extlibrary_Person> extlibrary_persons;


    public extlibrary_VideoCassette(
    ) {
        super(
        );
        this.extlibrary_persons = new ArrayList<>();
    }

    public extlibrary_VideoCassette(
        ArrayList<extlibrary_Person> extlibrary_persons    ) {
        this.extlibrary_persons = extlibrary_persons;
    }


    public List<extlibrary_Person> getExtlibrary_persons() {
        return extlibrary_persons;
    }

    public void addExtlibrary_person(Extlibrary_person extlibrary_person) {
        this.extlibrary_persons.add(extlibrary_person);
    }

}