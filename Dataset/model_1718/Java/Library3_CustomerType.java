





import java.util.List;
import java.util.ArrayList;

public class Library3_CustomerType  {

    private String firstName;
    private String lastName;
    private String borrowedBookId;



    public Library3_CustomerType(
        String firstName,        String lastName,        String borrowedBookId    ) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.borrowedBookId = borrowedBookId;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getBorrowedbookid() {
        return borrowedBookId;
    }

    public void setBorrowedbookid(String borrowedBookId) {
        this.borrowedBookId = borrowedBookId;
    }


}