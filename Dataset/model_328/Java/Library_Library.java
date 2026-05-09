





import java.util.List;
import java.util.ArrayList;

public class Library_Library  {

    private String name;
    private int id;





    private Library_Writer library_writer;




    private List<Library_Writer> library_writers;


    public Library_Library(
        String name,        int id    ) {
        this.name = name;
        this.id = id;
        this.library_writers = new ArrayList<>();
    }

    public Library_Library(
        String name,        int id        ArrayList<Library_Writer> library_writers    ) {
        this.name = name;
        this.id = id;
        this.library_writers = library_writers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Library_Writer getLibrary_writer() {
        return library_writer;
    }

    public void setLibrary_writer(Library_Writer library_writer) {
        this.library_writer = library_writer;
    }
    public List<Library_Writer> getLibrary_writers() {
        return library_writers;
    }

    public void addLibrary_writer(Library_writer library_writer) {
        this.library_writers.add(library_writer);
    }

}