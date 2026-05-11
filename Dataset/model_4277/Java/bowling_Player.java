




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Player  {

    private LocalDate dateOfBirth;
    private String name;
    private float height;
    private boolean isProfessional;



    public bowling_Player(
        LocalDate dateOfBirth,        String name,        float height,        boolean isProfessional    ) {
        this.dateOfBirth = dateOfBirth;
        this.name = name;
        this.height = height;
        this.isProfessional = isProfessional;
    }


    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public boolean getIsprofessional() {
        return isProfessional;
    }

    public void setIsprofessional(boolean isProfessional) {
        this.isProfessional = isProfessional;
    }


}