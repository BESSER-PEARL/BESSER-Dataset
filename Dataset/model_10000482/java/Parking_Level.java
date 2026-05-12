





import java.util.List;
import java.util.ArrayList;

public class Parking_Level  {

    private int Fl_Number;





    private Parking_Structure parking_structure;


    public Parking_Level(
        int Fl_Number    ) {
        this.Fl_Number = Fl_Number;
    }


    public int getFl_number() {
        return Fl_Number;
    }

    public void setFl_number(int Fl_Number) {
        this.Fl_Number = Fl_Number;
    }

    public Parking_Structure getParking_structure() {
        return parking_structure;
    }

    public void setParking_structure(Parking_Structure parking_structure) {
        this.parking_structure = parking_structure;
    }

}