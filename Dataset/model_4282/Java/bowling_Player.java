




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Player  {

    private String name;
    private boolean isProfessional;
    private LocalDate dateOfBirth;
    private float height;



    public bowling_Player(
        String name,        boolean isProfessional,        LocalDate dateOfBirth,        float height    ) {
        this.name = name;
        this.isProfessional = isProfessional;
        this.dateOfBirth = dateOfBirth;
        this.height = height;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsprofessional() {
        return isProfessional;
    }

    public void setIsprofessional(boolean isProfessional) {
        this.isProfessional = isProfessional;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }


}