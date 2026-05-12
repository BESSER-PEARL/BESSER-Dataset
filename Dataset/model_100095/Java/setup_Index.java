





import java.util.List;
import java.util.ArrayList;

public class setup_Index  {

    private String uRI;
    private String oldURIs;
    private String name;





    private setup_MetaIndex setup_metaindex;


    public setup_Index(
        String uRI,        String oldURIs,        String name    ) {
        this.uRI = uRI;
        this.oldURIs = oldURIs;
        this.name = name;
    }


    public String getUri() {
        return uRI;
    }

    public void setUri(String uRI) {
        this.uRI = uRI;
    }
    public String getOlduris() {
        return oldURIs;
    }

    public void setOlduris(String oldURIs) {
        this.oldURIs = oldURIs;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public setup_MetaIndex getSetup_metaindex() {
        return setup_metaindex;
    }

    public void setSetup_metaindex(setup_MetaIndex setup_metaindex) {
        this.setup_metaindex = setup_metaindex;
    }

}