





import java.util.List;
import java.util.ArrayList;

public class rdbmdl_Model extends NamedElement {

    private String server_id;



    public rdbmdl_Model(
        String server_id    ) {
        super(
        );
        this.server_id = server_id;
    }


    public String getServer_id() {
        return server_id;
    }

    public void setServer_id(String server_id) {
        this.server_id = server_id;
    }


}