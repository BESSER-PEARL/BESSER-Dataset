





import java.util.List;
import java.util.ArrayList;

public class parameterizedExpressionsTestLanguage_IdentifierRef extends Expression {

    private String id;



    public parameterizedExpressionsTestLanguage_IdentifierRef(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}