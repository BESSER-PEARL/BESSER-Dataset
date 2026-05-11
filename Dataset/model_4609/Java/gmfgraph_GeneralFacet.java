





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_GeneralFacet extends VisualFacet {

    private String data;
    private String identifier;



    public gmfgraph_GeneralFacet(
        String data,        String identifier    ) {
        super(
        );
        this.data = data;
        this.identifier = identifier;
    }


    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }


}