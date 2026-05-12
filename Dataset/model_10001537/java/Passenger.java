





import java.util.List;
import java.util.ArrayList;

public class Passenger  {

    private String name;





    private Luggage luggage;




    private CheckStaff checkstaff;


    public Passenger(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Luggage getLuggage() {
        return luggage;
    }

    public void setLuggage(Luggage luggage) {
        this.luggage = luggage;
    }
    public CheckStaff getCheckstaff() {
        return checkstaff;
    }

    public void setCheckstaff(CheckStaff checkstaff) {
        this.checkstaff = checkstaff;
    }

}