





import java.util.List;
import java.util.ArrayList;

public class operators_Marker extends Base {

    private String kind;
    private String description;





    private operators_NetXResource operators_netxresource;


    public operators_Marker(
        String kind,        String description    ) {
        super(
        );
        this.kind = kind;
        this.description = description;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public operators_NetXResource getOperators_netxresource() {
        return operators_netxresource;
    }

    public void setOperators_netxresource(operators_NetXResource operators_netxresource) {
        this.operators_netxresource = operators_netxresource;
    }

}