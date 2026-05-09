





import java.util.List;
import java.util.ArrayList;

public class library_Customer  {

    private String name;





    private List<library_Borrowable> library_borrowables;




    private library_Library library_library;


    public library_Customer(
        String name    ) {
        this.name = name;
        this.library_borrowables = new ArrayList<>();
    }

    public library_Customer(
        String name        ArrayList<library_Borrowable> library_borrowables    ) {
        this.name = name;
        this.library_borrowables = library_borrowables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<library_Borrowable> getLibrary_borrowables() {
        return library_borrowables;
    }

    public void addLibrary_borrowable(Library_borrowable library_borrowable) {
        this.library_borrowables.add(library_borrowable);
    }
    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }

}