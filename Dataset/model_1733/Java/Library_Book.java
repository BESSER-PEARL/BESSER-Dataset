





import java.util.List;
import java.util.ArrayList;

public class Library_Book  {

    private String name;





    private Library_Library library_library;


    public Library_Book(
        String name    ) {
        this.name = name;
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

}