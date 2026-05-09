





import java.util.List;
import java.util.ArrayList;

public class library3_CustomerType  {

    private String borrowedBookId;
    private String lastName;
    private String firstName;



    public library3_CustomerType(
        String borrowedBookId,        String lastName,        String firstName    ) {
        this.borrowedBookId = borrowedBookId;
        this.lastName = lastName;
        this.firstName = firstName;
    }


    public String getBorrowedbookid() {
        return borrowedBookId;
    }

    public void setBorrowedbookid(String borrowedBookId) {
        this.borrowedBookId = borrowedBookId;
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


}