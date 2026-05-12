




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private LocalDate primaryMemberDateOfBirth;



    public Customer(
        LocalDate primaryMemberDateOfBirth    ) {
        this.primaryMemberDateOfBirth = primaryMemberDateOfBirth;
    }


    public LocalDate getPrimarymemberdateofbirth() {
        return primaryMemberDateOfBirth;
    }

    public void setPrimarymemberdateofbirth(LocalDate primaryMemberDateOfBirth) {
        this.primaryMemberDateOfBirth = primaryMemberDateOfBirth;
    }


}