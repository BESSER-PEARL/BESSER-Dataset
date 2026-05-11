





import java.util.List;
import java.util.ArrayList;

public class pascal_output_value extends output_list {






    private List<pascal_output_value> pascal_output_values;


    public pascal_output_value(
    ) {
        super(
        );
        this.pascal_output_values = new ArrayList<>();
    }

    public pascal_output_value(
        ArrayList<pascal_output_value> pascal_output_values    ) {
        this.pascal_output_values = pascal_output_values;
    }


    public List<pascal_output_value> getPascal_output_values() {
        return pascal_output_values;
    }

    public void addPascal_output_value(Pascal_output_value pascal_output_value) {
        this.pascal_output_values.add(pascal_output_value);
    }

}