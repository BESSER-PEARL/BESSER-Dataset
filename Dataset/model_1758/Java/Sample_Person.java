





import java.util.List;
import java.util.ArrayList;

public class Sample_Person  {

    private String firstName;
    private String lastName;





    private Sample_Book sample_book;


    public Sample_Person(
        String firstName,        String lastName    ) {
        this.firstName = firstName;
        this.lastName = lastName;
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

    public Sample_Book getSample_book() {
        return sample_book;
    }

    public void setSample_book(Sample_Book sample_book) {
        this.sample_book = sample_book;
    }

}