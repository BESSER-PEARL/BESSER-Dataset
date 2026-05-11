





import java.util.List;
import java.util.ArrayList;

public class JavaSimplified_Field extends NamedElement, StringElement, CommentedElement, TypedElement {

    private String visibility;



    public JavaSimplified_Field(
        String visibility    ) {
        super(
        );
        this.visibility = visibility;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }


}