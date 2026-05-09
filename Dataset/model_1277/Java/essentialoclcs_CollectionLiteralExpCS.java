





import java.util.List;
import java.util.ArrayList;

public class essentialoclcs_CollectionLiteralExpCS extends LiteralExpCS {






    private List<essentialoclcs_CollectionLiteralPartCS> essentialoclcs_collectionliteralpartcss;




    private essentialoclcs_CollectionTypeCS essentialoclcs_collectiontypecs;


    public essentialoclcs_CollectionLiteralExpCS(
    ) {
        super(
        );
        this.essentialoclcs_collectionliteralpartcss = new ArrayList<>();
    }

    public essentialoclcs_CollectionLiteralExpCS(
        ArrayList<essentialoclcs_CollectionLiteralPartCS> essentialoclcs_collectionliteralpartcss    ) {
        this.essentialoclcs_collectionliteralpartcss = essentialoclcs_collectionliteralpartcss;
    }


    public List<essentialoclcs_CollectionLiteralPartCS> getEssentialoclcs_collectionliteralpartcss() {
        return essentialoclcs_collectionliteralpartcss;
    }

    public void addEssentialoclcs_collectionliteralpartcs(Essentialoclcs_collectionliteralpartcs essentialoclcs_collectionliteralpartcs) {
        this.essentialoclcs_collectionliteralpartcss.add(essentialoclcs_collectionliteralpartcs);
    }
    public essentialoclcs_CollectionTypeCS getEssentialoclcs_collectiontypecs() {
        return essentialoclcs_collectiontypecs;
    }

    public void setEssentialoclcs_collectiontypecs(essentialoclcs_CollectionTypeCS essentialoclcs_collectiontypecs) {
        this.essentialoclcs_collectiontypecs = essentialoclcs_collectiontypecs;
    }

}