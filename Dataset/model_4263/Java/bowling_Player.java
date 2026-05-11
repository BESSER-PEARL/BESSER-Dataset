




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Player  {

    private LocalDate dateOfBirth;
    private boolean isProfessional;
    private float height;
    private String name;



    public bowling_Player(
        LocalDate dateOfBirth,        boolean isProfessional,        float height,        String name    ) {
        this.dateOfBirth = dateOfBirth;
        this.isProfessional = isProfessional;
        this.height = height;
        this.name = name;
    }


    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}