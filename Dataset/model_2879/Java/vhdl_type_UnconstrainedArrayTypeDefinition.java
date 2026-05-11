





import java.util.List;
import java.util.ArrayList;

public class vhdl_type_UnconstrainedArrayTypeDefinition extends ArrayTypeDefinition {






    private List<TypeReference> typereferences;


    public vhdl_type_UnconstrainedArrayTypeDefinition(
    ) {
        super(
        );
        this.typereferences = new ArrayList<>();
    }

    public vhdl_type_UnconstrainedArrayTypeDefinition(
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