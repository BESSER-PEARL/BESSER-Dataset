





import java.util.List;
import java.util.ArrayList;

public class JavaSimplified_Method extends NamedElement, StringElement, CommentedElement {

    private String exceptions;





    private JavaSimplified_Type javasimplified_type;


    public JavaSimplified_Method(
        String exceptions    ) {
        super(
        );
        this.exceptions = exceptions;
    }


    public String getExceptions() {
        return exceptions;
    }

    public void setExceptions(String exceptions) {
        this.exceptions = exceptions;
    }

    public JavaSimplified_Type getJavasimplified_type() {
        return javasimplified_type;
    }

    public void setJavasimplified_type(JavaSimplified_Type javasimplified_type) {
        this.javasimplified_type = javasimplified_type;
    }

}