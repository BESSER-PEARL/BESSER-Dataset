





import java.util.List;
import java.util.ArrayList;

public class JTLMM_template_CollectionTemplateExp extends TemplateExp {

    private String kind;





    private CollectionType collectiontype;


    public JTLMM_template_CollectionTemplateExp(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public CollectionType getCollectiontype() {
        return collectiontype;
    }

    public void setCollectiontype(CollectionType collectiontype) {
        this.collectiontype = collectiontype;
    }

}