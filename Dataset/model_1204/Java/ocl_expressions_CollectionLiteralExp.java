





import java.util.List;
import java.util.ArrayList;

public class ocl_expressions_CollectionLiteralExp extends LiteralExp {

    private String kind;





    private List<CollectionLiteralPart> collectionliteralparts;


    public ocl_expressions_CollectionLiteralExp(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.collectionliteralparts = new ArrayList<>();
    }

    public ocl_expressions_CollectionLiteralExp(
        String kind        ArrayList<CollectionLiteralPart> collectionliteralparts    ) {
        this.kind = kind;
        this.collectionliteralparts = collectionliteralparts;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public List<CollectionLiteralPart> getCollectionliteralparts() {
        return collectionliteralparts;
    }

    public void addCollectionliteralpart(Collectionliteralpart collectionliteralpart) {
        this.collectionliteralparts.add(collectionliteralpart);
    }

}