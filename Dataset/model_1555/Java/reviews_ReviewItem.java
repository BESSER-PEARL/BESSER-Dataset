





import java.util.List;
import java.util.ArrayList;

public class reviews_ReviewItem extends CommentContainer {

    private String name;
    private String reference;
    private String id;



    public reviews_ReviewItem(
        String name,        String reference,        String id    ) {
        super(
        );
        this.name = name;
        this.reference = reference;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}