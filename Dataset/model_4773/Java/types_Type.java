





import java.util.List;
import java.util.ArrayList;

public class types_Type  {

    private String name;





    private types_TypeReference types_typereference;


    public types_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public types_TypeReference getTypes_typereference() {
        return types_typereference;
    }

    public void setTypes_typereference(types_TypeReference types_typereference) {
        this.types_typereference = types_typereference;
    }

}