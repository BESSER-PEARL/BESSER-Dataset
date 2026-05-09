





import java.util.List;
import java.util.ArrayList;

public class library_Library  {

    private String name;





    private List<library_Loan> library_loans;




    private library_UoD library_uod;


    public library_Library(
        String name    ) {
        this.name = name;
        this.library_loans = new ArrayList<>();
    }

    public library_Library(
        String name        ArrayList<library_Loan> library_loans    ) {
        this.name = name;
        this.library_loans = library_loans;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<library_Loan> getLibrary_loans() {
        return library_loans;
    }

    public void addLibrary_loan(Library_loan library_loan) {
        this.library_loans.add(library_loan);
    }
    public library_UoD getLibrary_uod() {
        return library_uod;
    }

    public void setLibrary_uod(library_UoD library_uod) {
        this.library_uod = library_uod;
    }

}