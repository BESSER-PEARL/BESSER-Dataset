





import java.util.List;
import java.util.ArrayList;

public class Party  {

    private int Number_Of_Adults;
    private int Number_of_Guests;
    private int Number_Of_Children;



    public Party(
        int Number_Of_Adults,        int Number_of_Guests,        int Number_Of_Children    ) {
        this.Number_Of_Adults = Number_Of_Adults;
        this.Number_of_Guests = Number_of_Guests;
        this.Number_Of_Children = Number_Of_Children;
    }


    public int getNumber_of_adults() {
        return Number_Of_Adults;
    }

    public void setNumber_of_adults(int Number_Of_Adults) {
        this.Number_Of_Adults = Number_Of_Adults;
    }
    public int getNumber_of_guests() {
        return Number_of_Guests;
    }

    public void setNumber_of_guests(int Number_of_Guests) {
        this.Number_of_Guests = Number_of_Guests;
    }
    public int getNumber_of_children() {
        return Number_Of_Children;
    }

    public void setNumber_of_children(int Number_Of_Children) {
        this.Number_Of_Children = Number_Of_Children;
    }


}