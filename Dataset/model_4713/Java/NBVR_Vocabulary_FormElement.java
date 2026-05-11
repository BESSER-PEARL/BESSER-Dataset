





import java.util.List;
import java.util.ArrayList;

public class NBVR_Vocabulary_FormElement  {

    private String kind;





    private SyntaxForm syntaxform;


    public NBVR_Vocabulary_FormElement(
        String kind    ) {
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public SyntaxForm getSyntaxform() {
        return syntaxform;
    }

    public void setSyntaxform(SyntaxForm syntaxform) {
        this.syntaxform = syntaxform;
    }

}