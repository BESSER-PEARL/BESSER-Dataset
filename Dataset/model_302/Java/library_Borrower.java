





import java.util.List;
import java.util.ArrayList;

public class library_Borrower extends Person {






    private library_Library library_library;




    private List<library_Lendable> library_lendables;




    private library_Lendable library_lendable;


    public library_Borrower(
    ) {
        super(
        );
        this.library_lendables = new ArrayList<>();
    }

    public library_Borrower(
        ArrayList<library_Lendable> library_lendables    ) {
        this.library_lendables = library_lendables;
    }


    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }
    public List<library_Lendable> getLibrary_lendables() {
        return library_lendables;
    }

    public void addLibrary_lendable(Library_lendable library_lendable) {
        this.library_lendables.add(library_lendable);
    }
    public library_Lendable getLibrary_lendable() {
        return library_lendable;
    }

    public void setLibrary_lendable(library_Lendable library_lendable) {
        this.library_lendable = library_lendable;
    }

}