




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class hairDressersRegSys_Person  {

    private String FirstName;
    private LocalDate DateOfBirth;
    private String Address;
    private String LastName;



    public hairDressersRegSys_Person(
        String FirstName,        LocalDate DateOfBirth,        String Address,        String LastName    ) {
        this.FirstName = FirstName;
        this.DateOfBirth = DateOfBirth;
        this.Address = Address;
        this.LastName = LastName;
    }


    public String getFirstname() {
        return FirstName;
    }

    public void setFirstname(String FirstName) {
        this.FirstName = FirstName;
    }
    public LocalDate getDateofbirth() {
        return DateOfBirth;
    }

    public void setDateofbirth(LocalDate DateOfBirth) {
        this.DateOfBirth = DateOfBirth;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getLastname() {
        return LastName;
    }

    public void setLastname(String LastName) {
        this.LastName = LastName;
    }


}