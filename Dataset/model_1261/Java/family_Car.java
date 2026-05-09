





import java.util.List;
import java.util.ArrayList;

public class family_Car  {

    private String numberOfSeats;





    private family_Person family_person;


    public family_Car(
        String numberOfSeats    ) {
        this.numberOfSeats = numberOfSeats;
    }


    public String getNumberofseats() {
        return numberOfSeats;
    }

    public void setNumberofseats(String numberOfSeats) {
        this.numberOfSeats = numberOfSeats;
    }

    public family_Person getFamily_person() {
        return family_person;
    }

    public void setFamily_person(family_Person family_person) {
        this.family_person = family_person;
    }

}