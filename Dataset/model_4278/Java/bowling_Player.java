




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Player  {

    private String name;
    private LocalDate dateOfBirth;



    public bowling_Player(
        String name,        LocalDate dateOfBirth    ) {
        this.name = name;
        this.dateOfBirth = dateOfBirth;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }


}