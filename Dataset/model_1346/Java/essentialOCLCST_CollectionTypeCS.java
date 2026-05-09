





import java.util.List;
import java.util.ArrayList;

public class essentialOCLCST_CollectionTypeCS extends TypeCS, TypeLiteralExpCS, CollectionLiteralExpCS {






    private List<essentialOCLCST_CollectionLiteralPartCS> essentialoclcst_collectionliteralpartcss;


    public essentialOCLCST_CollectionTypeCS(
    ) {
        super(
        );
        this.essentialoclcst_collectionliteralpartcss = new ArrayList<>();
    }

    public essentialOCLCST_CollectionTypeCS(
        ArrayList<essentialOCLCST_CollectionLiteralPartCS> essentialoclcst_collectionliteralpartcss    ) {
        this.essentialoclcst_collectionliteralpartcss = essentialoclcst_collectionliteralpartcss;
    }


    public List<essentialOCLCST_CollectionLiteralPartCS> getEssentialoclcst_collectionliteralpartcss() {
        return essentialoclcst_collectionliteralpartcss;
    }

    public void addEssentialoclcst_collectionliteralpartcs(Essentialoclcst_collectionliteralpartcs essentialoclcst_collectionliteralpartcs) {
        this.essentialoclcst_collectionliteralpartcss.add(essentialoclcst_collectionliteralpartcs);
    }

}