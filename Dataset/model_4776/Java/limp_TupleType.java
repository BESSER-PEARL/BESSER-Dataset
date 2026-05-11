





import java.util.List;
import java.util.ArrayList;

public class limp_TupleType extends Type {






    private List<limp_Type> limp_types;


    public limp_TupleType(
    ) {
        super(
        );
        this.limp_types = new ArrayList<>();
    }

    public limp_TupleType(
        ArrayList<limp_Type> limp_types    ) {
        this.limp_types = limp_types;
    }


    public List<limp_Type> getLimp_types() {
        return limp_types;
    }

    public void addLimp_type(Limp_type limp_type) {
        this.limp_types.add(limp_type);
    }

}