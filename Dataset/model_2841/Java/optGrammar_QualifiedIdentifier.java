





import java.util.List;
import java.util.ArrayList;

public class optGrammar_QualifiedIdentifier extends Expression, StandardType {

    private String identifier;



    public optGrammar_QualifiedIdentifier(
        String identifier    ) {
        super(
        );
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }


}