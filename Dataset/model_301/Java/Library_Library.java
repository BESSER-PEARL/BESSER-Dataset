





import java.util.List;
import java.util.ArrayList;

public class Library_Library extends Addressable {

    private String people;
    private String name;





    private Library_Library library_library;




    private List<Library_Writer> library_writers;




    private Library_Library library_library;


    public Library_Library(
        String people,        String name    ) {
        super(
        );
        this.people = people;
        this.name = name;
        this.library_writers = new ArrayList<>();
    }

    public Library_Library(
        String people,        String name        ArrayList<Library_Writer> library_writers    ) {
        this.people = people;
        this.name = name;
        this.library_writers = library_writers;
    }

    public String getPeople() {
        return people;
    }

    public void setPeople(String people) {
        this.people = people;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(Library_Library library_library) {
        this.library_library = library_library;
    }
    public List<Library_Writer> getLibrary_writers() {
        return library_writers;
    }

    public void addLibrary_writer(Library_writer library_writer) {
        this.library_writers.add(library_writer);
    }
    public Library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(Library_Library library_library) {
        this.library_library = library_library;
    }

}