




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Player  {

    private boolean isProfessional;
    private String name;
    private int streetNumber;
    private String street;
    private float height;
    private String eMail;
    private LocalDate dateOfBirth;



    public bowling_Player(
        boolean isProfessional,        String name,        int streetNumber,        String street,        float height,        String eMail,        LocalDate dateOfBirth    ) {
        this.isProfessional = isProfessional;
        this.name = name;
        this.streetNumber = streetNumber;
        this.street = street;
        this.height = height;
        this.eMail = eMail;
        this.dateOfBirth = dateOfBirth;
    }


    public boolean getIsprofessional() {
        return isProfessional;
    }

    public void setIsprofessional(boolean isProfessional) {
        this.isProfessional = isProfessional;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getStreetnumber() {
        return streetNumber;
    }

    public void setStreetnumber(int streetNumber) {
        this.streetNumber = streetNumber;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public String getEmail() {
        return eMail;
    }

    public void setEmail(String eMail) {
        this.eMail = eMail;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }


}