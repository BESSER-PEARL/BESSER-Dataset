





import java.util.List;
import java.util.ArrayList;

public class Parking_Level  {

    private int Fl_Number;





    private Parking_Structure parking_structure;




    private List<Boolean_external> boolean_externals;


    public Parking_Level(
        int Fl_Number    ) {
        this.Fl_Number = Fl_Number;
        this.boolean_externals = new ArrayList<>();
    }

    public Parking_Level(
        int Fl_Number        ArrayList<Boolean_external> boolean_externals    ) {
        this.Fl_Number = Fl_Number;
        this.boolean_externals = boolean_externals;
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
    public List<Boolean_external> getBoolean_externals() {
        return boolean_externals;
    }

    public void addBoolean_external(Boolean_external boolean_external) {
        this.boolean_externals.add(boolean_external);
    }

}