





import java.util.List;
import java.util.ArrayList;

public class extlibrary_Lendable  {

    private int copies;





    private List<extlibrary_Borrower> extlibrary_borrowers;




    private extlibrary_Borrower extlibrary_borrower;


    public extlibrary_Lendable(
        int copies    ) {
        this.copies = copies;
        this.extlibrary_borrowers = new ArrayList<>();
    }

    public extlibrary_Lendable(
        int copies        ArrayList<extlibrary_Borrower> extlibrary_borrowers    ) {
        this.copies = copies;
        this.extlibrary_borrowers = extlibrary_borrowers;
    }

    public int getCopies() {
        return copies;
    }

    public void setCopies(int copies) {
        this.copies = copies;
    }

    public List<extlibrary_Borrower> getExtlibrary_borrowers() {
        return extlibrary_borrowers;
    }

    public void addExtlibrary_borrower(Extlibrary_borrower extlibrary_borrower) {
        this.extlibrary_borrowers.add(extlibrary_borrower);
    }
    public extlibrary_Borrower getExtlibrary_borrower() {
        return extlibrary_borrower;
    }

    public void setExtlibrary_borrower(extlibrary_Borrower extlibrary_borrower) {
        this.extlibrary_borrower = extlibrary_borrower;
    }

}