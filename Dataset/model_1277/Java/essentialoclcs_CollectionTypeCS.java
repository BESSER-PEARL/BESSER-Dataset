





import java.util.List;
import java.util.ArrayList;

public class essentialoclcs_CollectionTypeCS extends TypedRefCS, Nameable {

    private String name;





    private essentialoclcs_CollectionPatternCS essentialoclcs_collectionpatterncs;


    public essentialoclcs_CollectionTypeCS(
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

    public essentialoclcs_CollectionPatternCS getEssentialoclcs_collectionpatterncs() {
        return essentialoclcs_collectionpatterncs;
    }

    public void setEssentialoclcs_collectionpatterncs(essentialoclcs_CollectionPatternCS essentialoclcs_collectionpatterncs) {
        this.essentialoclcs_collectionpatterncs = essentialoclcs_collectionpatterncs;
    }

}