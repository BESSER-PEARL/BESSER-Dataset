





import java.util.List;
import java.util.ArrayList;

public class backtrackingContentAssistTest_CollectionType extends TypeExp, CollectionLiteralExp {

    private String typeIdentifier;



    public backtrackingContentAssistTest_CollectionType(
        String typeIdentifier    ) {
        super(
        );
        this.typeIdentifier = typeIdentifier;
    }


    public String getTypeidentifier() {
        return typeIdentifier;
    }

    public void setTypeidentifier(String typeIdentifier) {
        this.typeIdentifier = typeIdentifier;
    }


}