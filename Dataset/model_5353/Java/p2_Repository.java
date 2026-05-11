





import java.util.List;
import java.util.ArrayList;

public class p2_Repository extends ModelElement {

    private String type;
    private String uRL;





    private p2_ProfileDefinition p2_profiledefinition;




    private p2_RepositoryList p2_repositorylist;


    public p2_Repository(
        String type,        String uRL    ) {
        super(
        );
        this.type = type;
        this.uRL = uRL;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getUrl() {
        return uRL;
    }

    public void setUrl(String uRL) {
        this.uRL = uRL;
    }

    public p2_ProfileDefinition getP2_profiledefinition() {
        return p2_profiledefinition;
    }

    public void setP2_profiledefinition(p2_ProfileDefinition p2_profiledefinition) {
        this.p2_profiledefinition = p2_profiledefinition;
    }
    public p2_RepositoryList getP2_repositorylist() {
        return p2_repositorylist;
    }

    public void setP2_repositorylist(p2_RepositoryList p2_repositorylist) {
        this.p2_repositorylist = p2_repositorylist;
    }

}