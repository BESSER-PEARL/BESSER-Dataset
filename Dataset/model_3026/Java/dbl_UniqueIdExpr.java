





import java.util.List;
import java.util.ArrayList;

public class dbl_UniqueIdExpr extends Expression {

    private String identifier;



    public dbl_UniqueIdExpr(
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