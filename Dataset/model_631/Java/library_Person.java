





import java.util.List;
import java.util.ArrayList;

public class library_Person extends AbstractPerson {






    private library_Loan library_loan;


    public library_Person(
    ) {
        super(
        );
    }



    public library_Loan getLibrary_loan() {
        return library_loan;
    }

    public void setLibrary_loan(library_Loan library_loan) {
        this.library_loan = library_loan;
    }

}