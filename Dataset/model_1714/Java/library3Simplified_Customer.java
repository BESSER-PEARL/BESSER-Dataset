





import java.util.List;
import java.util.ArrayList;

public class library3Simplified_Customer  {

    private String borrowedBookSince;
    private String lastName;
    private String firstName;





    private library3Simplified_Book library3simplified_book;


    public library3Simplified_Customer(
        String borrowedBookSince,        String lastName,        String firstName    ) {
        this.borrowedBookSince = borrowedBookSince;
        this.lastName = lastName;
        this.firstName = firstName;
    }


    public String getBorrowedbooksince() {
        return borrowedBookSince;
    }

    public void setBorrowedbooksince(String borrowedBookSince) {
        this.borrowedBookSince = borrowedBookSince;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public library3Simplified_Book getLibrary3simplified_book() {
        return library3simplified_book;
    }

    public void setLibrary3simplified_book(library3Simplified_Book library3simplified_book) {
        this.library3simplified_book = library3simplified_book;
    }

}