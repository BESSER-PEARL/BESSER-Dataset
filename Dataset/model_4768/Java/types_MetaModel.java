





import java.util.List;
import java.util.ArrayList;

public class types_MetaModel  {

    private String name;





    private types_Metaclass types_metaclass;


    public types_MetaModel(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public types_Metaclass getTypes_metaclass() {
        return types_metaclass;
    }

    public void setTypes_metaclass(types_Metaclass types_metaclass) {
        this.types_metaclass = types_metaclass;
    }

}