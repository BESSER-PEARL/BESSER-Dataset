





import java.util.List;
import java.util.ArrayList;

public class kermeta_behavior_VariableDecl extends Expression {

    private String identifier;



    public kermeta_behavior_VariableDecl(
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