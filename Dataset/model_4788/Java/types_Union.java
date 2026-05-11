





import java.util.List;
import java.util.ArrayList;

public class types_Union extends Type {

    private String name;





    private types_Field types_field;




    private types_Type types_type;




    private List<types_Branch> types_branchs;


    public types_Union(
        String name    ) {
        super(
        );
        this.name = name;
        this.types_branchs = new ArrayList<>();
    }

    public types_Union(
        String name        ArrayList<types_Branch> types_branchs    ) {
        this.name = name;
        this.types_branchs = types_branchs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public types_Field getTypes_field() {
        return types_field;
    }

    public void setTypes_field(types_Field types_field) {
        this.types_field = types_field;
    }
    public types_Type getTypes_type() {
        return types_type;
    }

    public void setTypes_type(types_Type types_type) {
        this.types_type = types_type;
    }
    public List<types_Branch> getTypes_branchs() {
        return types_branchs;
    }

    public void addTypes_branch(Types_branch types_branch) {
        this.types_branchs.add(types_branch);
    }

}