





import java.util.List;
import java.util.ArrayList;

public class essentialoclcs_CollectionTypeCS extends Nameable, TypedRefCS {

    private String name;





    private essentialoclcs_CollectionLiteralExpCS essentialoclcs_collectionliteralexpcs;


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

    public essentialoclcs_CollectionLiteralExpCS getEssentialoclcs_collectionliteralexpcs() {
        return essentialoclcs_collectionliteralexpcs;
    }

    public void setEssentialoclcs_collectionliteralexpcs(essentialoclcs_CollectionLiteralExpCS essentialoclcs_collectionliteralexpcs) {
        this.essentialoclcs_collectionliteralexpcs = essentialoclcs_collectionliteralexpcs;
    }

}