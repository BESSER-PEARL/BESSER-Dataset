





import java.util.List;
import java.util.ArrayList;

public class rell_PrimitiveType  {

    private String primitiveType;





    private rell_TypeReference rell_typereference;


    public rell_PrimitiveType(
        String primitiveType    ) {
        this.primitiveType = primitiveType;
    }


    public String getPrimitivetype() {
        return primitiveType;
    }

    public void setPrimitivetype(String primitiveType) {
        this.primitiveType = primitiveType;
    }

    public rell_TypeReference getRell_typereference() {
        return rell_typereference;
    }

    public void setRell_typereference(rell_TypeReference rell_typereference) {
        this.rell_typereference = rell_typereference;
    }

}