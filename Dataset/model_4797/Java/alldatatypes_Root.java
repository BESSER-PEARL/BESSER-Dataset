





import java.util.List;
import java.util.ArrayList;

public class alldatatypes_Root extends Element {






    private List<alldatatypes_Type> alldatatypes_types;


    public alldatatypes_Root(
    ) {
        super(
        );
        this.alldatatypes_types = new ArrayList<>();
    }

    public alldatatypes_Root(
        ArrayList<alldatatypes_Type> alldatatypes_types    ) {
        this.alldatatypes_types = alldatatypes_types;
    }


    public List<alldatatypes_Type> getAlldatatypes_types() {
        return alldatatypes_types;
    }

    public void addAlldatatypes_type(Alldatatypes_type alldatatypes_type) {
        this.alldatatypes_types.add(alldatatypes_type);
    }

}