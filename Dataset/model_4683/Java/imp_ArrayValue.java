





import java.util.List;
import java.util.ArrayList;

public class imp_ArrayValue extends Value {






    private List<imp_Value> imp_values;


    public imp_ArrayValue(
    ) {
        super(
        );
        this.imp_values = new ArrayList<>();
    }

    public imp_ArrayValue(
        ArrayList<imp_Value> imp_values    ) {
        this.imp_values = imp_values;
    }


    public List<imp_Value> getImp_values() {
        return imp_values;
    }

    public void addImp_value(Imp_value imp_value) {
        this.imp_values.add(imp_value);
    }

}