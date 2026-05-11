





import java.util.List;
import java.util.ArrayList;

public class JavaSimplified_Name extends Expression {

    private String identifier;



    public JavaSimplified_Name(
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