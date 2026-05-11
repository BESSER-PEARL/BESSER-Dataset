





import java.util.List;
import java.util.ArrayList;

public class atl_types_UnionType extends Type {






    private List<atl_types_Type> atl_types_types;


    public atl_types_UnionType(
    ) {
        super(
        );
        this.atl_types_types = new ArrayList<>();
    }

    public atl_types_UnionType(
        ArrayList<atl_types_Type> atl_types_types    ) {
        this.atl_types_types = atl_types_types;
    }


    public List<atl_types_Type> getAtl_types_types() {
        return atl_types_types;
    }

    public void addAtl_types_type(Atl_types_type atl_types_type) {
        this.atl_types_types.add(atl_types_type);
    }

}