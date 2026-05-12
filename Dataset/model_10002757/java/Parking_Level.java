





import java.util.List;
import java.util.ArrayList;

public class Parking_Level  {

    private int Fl_Number;





    private List<Boolean_external> boolean_externals;




    private Parking_Structure parking_structure;


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

    public List<Boolean_external> getBoolean_externals() {
        return boolean_externals;
    }

    public void addBoolean_external(Boolean_external boolean_external) {
        this.boolean_externals.add(boolean_external);
    }
    public Parking_Structure getParking_structure() {
        return parking_structure;
    }

    public void setParking_structure(Parking_Structure parking_structure) {
        this.parking_structure = parking_structure;
    }

}