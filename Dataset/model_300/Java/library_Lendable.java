





import java.util.List;
import java.util.ArrayList;

public class library_Lendable  {

    private int copies;





    private library_Borrower library_borrower;




    private List<library_Borrower> library_borrowers;


    public library_Lendable(
        int copies    ) {
        this.copies = copies;
        this.library_borrowers = new ArrayList<>();
    }

    public library_Lendable(
        int copies        ArrayList<library_Borrower> library_borrowers    ) {
        this.copies = copies;
        this.library_borrowers = library_borrowers;
    }

    public int getCopies() {
        return copies;
    }

    public void setCopies(int copies) {
        this.copies = copies;
    }

    public library_Borrower getLibrary_borrower() {
        return library_borrower;
    }

    public void setLibrary_borrower(library_Borrower library_borrower) {
        this.library_borrower = library_borrower;
    }
    public List<library_Borrower> getLibrary_borrowers() {
        return library_borrowers;
    }

    public void addLibrary_borrower(Library_borrower library_borrower) {
        this.library_borrowers.add(library_borrower);
    }

}