





import java.util.List;
import java.util.ArrayList;

public class library3Simplified_Customer  {

    private String lastName;
    private String borrowedBookSince;
    private String firstName;



    public library3Simplified_Customer(
        String lastName,        String borrowedBookSince,        String firstName    ) {
        this.lastName = lastName;
        this.borrowedBookSince = borrowedBookSince;
        this.firstName = firstName;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getBorrowedbooksince() {
        return borrowedBookSince;
    }

    public void setBorrowedbooksince(String borrowedBookSince) {
        this.borrowedBookSince = borrowedBookSince;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }


}