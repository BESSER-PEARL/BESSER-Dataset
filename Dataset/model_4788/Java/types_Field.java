





import java.util.List;
import java.util.ArrayList;

public class types_Field  {

    private String name;





    private types_Type types_type;




    private types_Branch types_branch;




    private types_Key types_key;


    public types_Field(
        String name    ) {
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
    public types_Branch getTypes_branch() {
        return types_branch;
    }

    public void setTypes_branch(types_Branch types_branch) {
        this.types_branch = types_branch;
    }
    public types_Key getTypes_key() {
        return types_key;
    }

    public void setTypes_key(types_Key types_key) {
        this.types_key = types_key;
    }

}