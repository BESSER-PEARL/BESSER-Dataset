





import java.util.List;
import java.util.ArrayList;

public class expansionmodel_GMFT_BasedRepresentation extends Representation {

    private String reusedID;





    private expansionmodel_UseContext expansionmodel_usecontext;


    public expansionmodel_GMFT_BasedRepresentation(
        String reusedID    ) {
        super(
        );
        this.reusedID = reusedID;
    }


    public String getReusedid() {
        return reusedID;
    }

    public void setReusedid(String reusedID) {
        this.reusedID = reusedID;
    }

    public expansionmodel_UseContext getExpansionmodel_usecontext() {
        return expansionmodel_usecontext;
    }

    public void setExpansionmodel_usecontext(expansionmodel_UseContext expansionmodel_usecontext) {
        this.expansionmodel_usecontext = expansionmodel_usecontext;
    }

}