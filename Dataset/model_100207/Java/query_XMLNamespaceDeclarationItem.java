





import java.util.List;
import java.util.ArrayList;

public class query_XMLNamespaceDeclarationItem extends SQLQueryObject {

    private String uri;



    public query_XMLNamespaceDeclarationItem(
        String uri    ) {
        super(
        );
        this.uri = uri;
    }


    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }


}