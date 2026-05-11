





import java.util.List;
import java.util.ArrayList;

public class miniJava_ArrayInstance  {

    private int size;





    private List<miniJava_Value> minijava_values;




    private miniJava_State minijava_state;




    private miniJava_ArrayRefValue minijava_arrayrefvalue;


    public miniJava_ArrayInstance(
        int size    ) {
        this.size = size;
        this.minijava_values = new ArrayList<>();
    }

    public miniJava_ArrayInstance(
        int size        ArrayList<miniJava_Value> minijava_values    ) {
        this.size = size;
        this.minijava_values = minijava_values;
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public List<miniJava_Value> getMinijava_values() {
        return minijava_values;
    }

    public void addMinijava_value(Minijava_value minijava_value) {
        this.minijava_values.add(minijava_value);
    }
    public miniJava_State getMinijava_state() {
        return minijava_state;
    }

    public void setMinijava_state(miniJava_State minijava_state) {
        this.minijava_state = minijava_state;
    }
    public miniJava_ArrayRefValue getMinijava_arrayrefvalue() {
        return minijava_arrayrefvalue;
    }

    public void setMinijava_arrayrefvalue(miniJava_ArrayRefValue minijava_arrayrefvalue) {
        this.minijava_arrayrefvalue = minijava_arrayrefvalue;
    }

}