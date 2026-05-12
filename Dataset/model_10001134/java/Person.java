




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String State;
    private String firstName;
    private String middleName;
    private String cellPhone;
    private String note;
    private String city;
    private String lastName;
    private String homePhone;
    private LocalDate DoB;
    private String email;
    private String address;



    public Person(
        String State,        String firstName,        String middleName,        String cellPhone,        String note,        String city,        String lastName,        String homePhone,        LocalDate DoB,        String email,        String address    ) {
        this.State = State;
        this.firstName = firstName;
        this.middleName = middleName;
        this.cellPhone = cellPhone;
        this.note = note;
        this.city = city;
        this.lastName = lastName;
        this.homePhone = homePhone;
        this.DoB = DoB;
        this.email = email;
        this.address = address;
    }


    public String getState() {
        return State;
    }

    public void setState(String State) {
        this.State = State;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getMiddlename() {
        return middleName;
    }

    public void setMiddlename(String middleName) {
        this.middleName = middleName;
    }
    public String getCellphone() {
        return cellPhone;
    }

    public void setCellphone(String cellPhone) {
        this.cellPhone = cellPhone;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getHomephone() {
        return homePhone;
    }

    public void setHomephone(String homePhone) {
        this.homePhone = homePhone;
    }
    public LocalDate getDob() {
        return DoB;
    }

    public void setDob(LocalDate DoB) {
        this.DoB = DoB;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}