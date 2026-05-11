





import java.util.List;
import java.util.ArrayList;

public class JavaSimplified_Feature extends StringElement, CommentedElement, NamedElement {

    private String visibility;



    public JavaSimplified_Feature(
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