





import java.util.List;
import java.util.ArrayList;

public class minioclcs_CollectionLiteralExpCS extends LiteralExpCS {

    private String kind;





    private List<minioclcs_CollectionLiteralPartCS> minioclcs_collectionliteralpartcss;


    public minioclcs_CollectionLiteralExpCS(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.minioclcs_collectionliteralpartcss = new ArrayList<>();
    }

    public minioclcs_CollectionLiteralExpCS(
        String kind        ArrayList<minioclcs_CollectionLiteralPartCS> minioclcs_collectionliteralpartcss    ) {
        this.kind = kind;
        this.minioclcs_collectionliteralpartcss = minioclcs_collectionliteralpartcss;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public List<minioclcs_CollectionLiteralPartCS> getMinioclcs_collectionliteralpartcss() {
        return minioclcs_collectionliteralpartcss;
    }

    public void addMinioclcs_collectionliteralpartcs(Minioclcs_collectionliteralpartcs minioclcs_collectionliteralpartcs) {
        this.minioclcs_collectionliteralpartcss.add(minioclcs_collectionliteralpartcs);
    }

}