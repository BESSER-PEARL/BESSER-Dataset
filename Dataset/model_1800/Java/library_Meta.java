





import java.util.List;
import java.util.ArrayList;

public class library_Meta  {

    private String version;
    private String description;
    private String author;





    private library_Library library_library;


    public library_Meta(
        String version,        String description,        String author    ) {
        this.version = version;
        this.description = description;
        this.author = author;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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