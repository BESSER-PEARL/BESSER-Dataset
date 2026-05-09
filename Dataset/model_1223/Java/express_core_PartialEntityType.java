





import java.util.List;
import java.util.ArrayList;

public class express_core_PartialEntityType extends DataType {






    private List<SingleEntityType> singleentitytypes;


    public express_core_PartialEntityType(
    ) {
        super(
        );
        this.singleentitytypes = new ArrayList<>();
    }

    public express_core_PartialEntityType(
        ArrayList<SingleEntityType> singleentitytypes    ) {
        this.singleentitytypes = singleentitytypes;
    }


    public List<SingleEntityType> getSingleentitytypes() {
        return singleentitytypes;
    }

    public void addSingleentitytype(Singleentitytype singleentitytype) {
        this.singleentitytypes.add(singleentitytype);
    }

}