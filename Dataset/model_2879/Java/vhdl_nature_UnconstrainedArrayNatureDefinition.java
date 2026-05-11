





import java.util.List;
import java.util.ArrayList;

public class vhdl_nature_UnconstrainedArrayNatureDefinition extends ArrayNatureDefinition {






    private List<TypeReference> typereferences;


    public vhdl_nature_UnconstrainedArrayNatureDefinition(
    ) {
        super(
        );
        this.typereferences = new ArrayList<>();
    }

    public vhdl_nature_UnconstrainedArrayNatureDefinition(
        ArrayList<TypeReference> typereferences    ) {
        this.typereferences = typereferences;
    }


    public List<TypeReference> getTypereferences() {
        return typereferences;
    }

    public void addTypereference(Typereference typereference) {
        this.typereferences.add(typereference);
    }

}