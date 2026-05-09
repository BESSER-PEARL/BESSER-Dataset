





import java.util.List;
import java.util.ArrayList;

public class graph_ElkGraphElement extends EMapPropertyHolder {

    private String identifier;



    public graph_ElkGraphElement(
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