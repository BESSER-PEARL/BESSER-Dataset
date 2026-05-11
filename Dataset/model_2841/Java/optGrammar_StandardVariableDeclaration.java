





import java.util.List;
import java.util.ArrayList;

public class optGrammar_StandardVariableDeclaration extends SimpleStatement, SimpleStatement2 {

    private boolean semicolon;





    private optGrammar_StandardTypeWithoutQualifiedIdentifier optgrammar_standardtypewithoutqualifiedidentifier;


    public optGrammar_StandardVariableDeclaration(
        boolean semicolon    ) {
        super(
        );
        this.semicolon = semicolon;
    }


    public boolean getSemicolon() {
        return semicolon;
    }

    public void setSemicolon(boolean semicolon) {
        this.semicolon = semicolon;
    }

    public optGrammar_StandardTypeWithoutQualifiedIdentifier getOptgrammar_standardtypewithoutqualifiedidentifier() {
        return optgrammar_standardtypewithoutqualifiedidentifier;
    }

    public void setOptgrammar_standardtypewithoutqualifiedidentifier(optGrammar_StandardTypeWithoutQualifiedIdentifier optgrammar_standardtypewithoutqualifiedidentifier) {
        this.optgrammar_standardtypewithoutqualifiedidentifier = optgrammar_standardtypewithoutqualifiedidentifier;
    }

}