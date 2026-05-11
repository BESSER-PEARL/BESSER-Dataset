




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Player  {

    private LocalDate dateOfBirth;
    private String name;



    public bowling_Player(
        LocalDate dateOfBirth,        String name    ) {
        this.dateOfBirth = dateOfBirth;
        this.name = name;
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


}