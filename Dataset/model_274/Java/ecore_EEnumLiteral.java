





import java.util.List;
import java.util.ArrayList;

public class ecore_EEnumLiteral extends ENamedElement {

    private String literal;



    public ecore_EEnumLiteral(
        String literal    ) {
        super(
        );
        this.literal = literal;
    }


    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }


}