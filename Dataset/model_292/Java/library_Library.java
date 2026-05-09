





import java.util.List;
import java.util.ArrayList;

public class library_Library extends Identifiable {

    private String name;





    private List<library_Writer> library_writers;


    public library_Library(
        String name    ) {
        super(
        );
        this.name = name;
        this.library_writers = new ArrayList<>();
    }

    public library_Library(
        String name        ArrayList<library_Writer> library_writers    ) {
        this.name = name;
        this.library_writers = library_writers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<library_Writer> getLibrary_writers() {
        return library_writers;
    }

    public void addLibrary_writer(Library_writer library_writer) {
        this.library_writers.add(library_writer);
    }

}