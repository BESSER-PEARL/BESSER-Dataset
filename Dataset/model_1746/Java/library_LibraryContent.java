





import java.util.List;
import java.util.ArrayList;

public class library_LibraryContent  {

    private String name;
    private String author;





    private library_Library library_library;


    public library_LibraryContent(
        String name,        String author    ) {
        this.name = name;
        this.author = author;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }

}