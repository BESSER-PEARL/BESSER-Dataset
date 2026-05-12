





import java.util.List;
import java.util.ArrayList;

public class librarian  {

    private String name;





    private library library;


    public librarian(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public library getLibrary() {
        return library;
    }

    public void setLibrary(library library) {
        this.library = library;
    }

}