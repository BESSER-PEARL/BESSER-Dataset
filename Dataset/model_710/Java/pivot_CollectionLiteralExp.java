





import java.util.List;
import java.util.ArrayList;

public class pivot_CollectionLiteralExp extends LiteralExp {

    private String kind;





    private List<pivot_CollectionLiteralPart> pivot_collectionliteralparts;


    public pivot_CollectionLiteralExp(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.pivot_collectionliteralparts = new ArrayList<>();
    }

    public pivot_CollectionLiteralExp(
        String kind        ArrayList<pivot_CollectionLiteralPart> pivot_collectionliteralparts    ) {
        this.kind = kind;
        this.pivot_collectionliteralparts = pivot_collectionliteralparts;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public List<pivot_CollectionLiteralPart> getPivot_collectionliteralparts() {
        return pivot_collectionliteralparts;
    }

    public void addPivot_collectionliteralpart(Pivot_collectionliteralpart pivot_collectionliteralpart) {
        this.pivot_collectionliteralparts.add(pivot_collectionliteralpart);
    }

}