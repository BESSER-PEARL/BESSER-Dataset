





import java.util.List;
import java.util.ArrayList;

public class emof_NamedElement extends Element {

    private String name;





    private emof_Comment emof_comment;


    public emof_NamedElement(
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

    public emof_Comment getEmof_comment() {
        return emof_comment;
    }

    public void setEmof_comment(emof_Comment emof_comment) {
        this.emof_comment = emof_comment;
    }

}