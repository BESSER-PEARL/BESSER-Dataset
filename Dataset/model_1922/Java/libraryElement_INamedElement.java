





import java.util.List;
import java.util.ArrayList;

public class libraryElement_INamedElement extends I4DIACElement {

    private String name;
    private String comment;



    public libraryElement_INamedElement(
        String name,        String comment    ) {
        super(
        );
        this.name = name;
        this.comment = comment;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}