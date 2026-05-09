





import java.util.List;
import java.util.ArrayList;

public class minioclcs_ImportCS extends CSTrace {

    private String alias;
    private String uri;





    private minioclcs_RootCS minioclcs_rootcs;


    public minioclcs_ImportCS(
        String alias,        String uri    ) {
        super(
        );
        this.alias = alias;
        this.uri = uri;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }

    public minioclcs_RootCS getMinioclcs_rootcs() {
        return minioclcs_rootcs;
    }

    public void setMinioclcs_rootcs(minioclcs_RootCS minioclcs_rootcs) {
        this.minioclcs_rootcs = minioclcs_rootcs;
    }

}