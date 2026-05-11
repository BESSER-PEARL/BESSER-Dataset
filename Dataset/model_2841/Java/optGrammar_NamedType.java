





import java.util.List;
import java.util.ArrayList;

public class optGrammar_NamedType extends StandardTypeWithoutQualifiedIdentifier, StandardType {

    private String type;



    public optGrammar_NamedType(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}