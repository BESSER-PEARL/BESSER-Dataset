




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Player  {

    private String name;
    private boolean isProfessional;
    private float height;
    private LocalDate dateOfBirth;



    public bowling_Player(
        String name,        boolean isProfessional,        float height,        LocalDate dateOfBirth    ) {
        this.name = name;
        this.isProfessional = isProfessional;
        this.height = height;
        this.dateOfBirth = dateOfBirth;
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
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }


}