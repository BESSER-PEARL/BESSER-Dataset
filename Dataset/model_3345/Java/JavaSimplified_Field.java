





import java.util.List;
import java.util.ArrayList;

public class JavaSimplified_Field extends CommentedElement, TypedElement, NamedElement, StringElement {

    private String visibility;





    private JavaSimplified_Expression javasimplified_expression;


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

    public JavaSimplified_Expression getJavasimplified_expression() {
        return javasimplified_expression;
    }

    public void setJavasimplified_expression(JavaSimplified_Expression javasimplified_expression) {
        this.javasimplified_expression = javasimplified_expression;
    }

}