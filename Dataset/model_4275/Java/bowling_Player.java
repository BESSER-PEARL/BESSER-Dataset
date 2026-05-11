




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Player  {

    private String street;
    private String name;
    private String telephon;
    private String notes;
    private LocalDate dateOfBirth;
    private String eMail;
    private int streetNumber;
    private boolean isProfessional;
    private float height;
    private boolean isAvailable;



    public bowling_Player(
        String street,        String name,        String telephon,        String notes,        LocalDate dateOfBirth,        String eMail,        int streetNumber,        boolean isProfessional,        float height,        boolean isAvailable    ) {
        this.street = street;
        this.name = name;
        this.telephon = telephon;
        this.notes = notes;
        this.dateOfBirth = dateOfBirth;
        this.eMail = eMail;
        this.streetNumber = streetNumber;
        this.isProfessional = isProfessional;
        this.height = height;
        this.isAvailable = isAvailable;
    }


    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTelephon() {
        return telephon;
    }

    public void setTelephon(String telephon) {
        this.telephon = telephon;
    }
    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getEmail() {
        return eMail;
    }

    public void setEmail(String eMail) {
        this.eMail = eMail;
    }
    public int getStreetnumber() {
        return streetNumber;
    }

    public void setStreetnumber(int streetNumber) {
        this.streetNumber = streetNumber;
    }
    public boolean getIsprofessional() {
        return isProfessional;
    }

    public void setIsprofessional(boolean isProfessional) {
        this.isProfessional = isProfessional;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public boolean getIsavailable() {
        return isAvailable;
    }

    public void setIsavailable(boolean isAvailable) {
        this.isAvailable = isAvailable;
    }


}