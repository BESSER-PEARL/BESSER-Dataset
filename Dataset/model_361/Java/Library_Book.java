





import java.util.List;
import java.util.ArrayList;

public class Library_Book  {

    private String title;





    private Library_Library library_library;




    private Library_Writer library_writer;




    private List<Library_Writer> library_writers;


    public Library_Book(
        String title    ) {
        this.title = title;
        this.library_writers = new ArrayList<>();
    }

    public Library_Book(
        String title        ArrayList<Library_Writer> library_writers    ) {
        this.title = title;
        this.library_writers = library_writers;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(Library_Library library_library) {
        this.library_library = library_library;
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