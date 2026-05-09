





import java.util.List;
import java.util.ArrayList;

public class Library_Lendable  {

    private int copies;





    private List<Library_Borrower> library_borrowers;




    private Library_Borrower library_borrower;


    public Library_Lendable(
        int copies    ) {
        this.copies = copies;
        this.library_borrowers = new ArrayList<>();
    }

    public Library_Lendable(
        int copies        ArrayList<Library_Borrower> library_borrowers    ) {
        this.copies = copies;
        this.library_borrowers = library_borrowers;
    }

    public int getCopies() {
        return copies;
    }

    public void setCopies(int copies) {
        this.copies = copies;
    }

    public List<Library_Borrower> getLibrary_borrowers() {
        return library_borrowers;
    }

    public void addLibrary_borrower(Library_borrower library_borrower) {
        this.library_borrowers.add(library_borrower);
    }
    public Library_Borrower getLibrary_borrower() {
        return library_borrower;
    }

    public void setLibrary_borrower(Library_Borrower library_borrower) {
        this.library_borrower = library_borrower;
    }

}