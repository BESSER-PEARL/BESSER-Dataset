





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_GeneralFacet extends VisualFacet {

    private String identifier;
    private String data;



    public gmfgraph_GeneralFacet(
        String identifier,        String data    ) {
        super(
        );
        this.identifier = identifier;
        this.data = data;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }


}