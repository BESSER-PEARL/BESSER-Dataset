





import java.util.List;
import java.util.ArrayList;

public class types_Typedef extends Type {

    private String name;





    private types_Type types_type;


    public types_Typedef(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public types_Type getTypes_type() {
        return types_type;
    }

    public void setTypes_type(types_Type types_type) {
        this.types_type = types_type;
    }

}