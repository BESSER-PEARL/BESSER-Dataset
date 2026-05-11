





import java.util.List;
import java.util.ArrayList;

public class archimate_Outcome extends MotivationElement {






    private List<archimate_Value> archimate_values;




    private archimate_Value archimate_value;


    public archimate_Outcome(
    ) {
        super(
        );
        this.archimate_values = new ArrayList<>();
    }

    public archimate_Outcome(
        ArrayList<archimate_Value> archimate_values    ) {
        this.archimate_values = archimate_values;
    }


    public List<archimate_Value> getArchimate_values() {
        return archimate_values;
    }

    public void addArchimate_value(Archimate_value archimate_value) {
        this.archimate_values.add(archimate_value);
    }
    public archimate_Value getArchimate_value() {
        return archimate_value;
    }

    public void setArchimate_value(archimate_Value archimate_value) {
        this.archimate_value = archimate_value;
    }

}