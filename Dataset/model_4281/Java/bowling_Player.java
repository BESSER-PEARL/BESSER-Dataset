




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Player  {

    private float height;
    private String city;
    private String firstname;
    private String lastname;
    private boolean isProfessional;
    private int streetnumber;
    private LocalDate dateOfBirth;
    private String street;



    public bowling_Player(
        float height,        String city,        String firstname,        String lastname,        boolean isProfessional,        int streetnumber,        LocalDate dateOfBirth,        String street    ) {
        this.height = height;
        this.city = city;
        this.firstname = firstname;
        this.lastname = lastname;
        this.isProfessional = isProfessional;
        this.streetnumber = streetnumber;
        this.dateOfBirth = dateOfBirth;
        this.street = street;
    }


    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public boolean getIsprofessional() {
        return isProfessional;
    }

    public void setIsprofessional(boolean isProfessional) {
        this.isProfessional = isProfessional;
    }
    public int getStreetnumber() {
        return streetnumber;
    }

    public void setStreetnumber(int streetnumber) {
        this.streetnumber = streetnumber;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }


}