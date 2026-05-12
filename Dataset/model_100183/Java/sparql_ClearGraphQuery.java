





import java.util.List;
import java.util.ArrayList;

public class sparql_ClearGraphQuery extends UpdateOperation {

    private String uri;
    private boolean isDefault;



    public sparql_ClearGraphQuery(
        String uri,        boolean isDefault    ) {
        super(
        );
        this.uri = uri;
        this.isDefault = isDefault;
    }


    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public boolean getIsdefault() {
        return isDefault;
    }

    public void setIsdefault(boolean isDefault) {
        this.isDefault = isDefault;
    }


}