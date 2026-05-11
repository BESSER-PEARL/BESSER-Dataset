





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Architecture  {

    private String ID;





    private contentfwk_EnterpriseArchitecture contentfwk_enterprisearchitecture;


    public contentfwk_Architecture(
        String ID    ) {
        this.ID = ID;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public contentfwk_EnterpriseArchitecture getContentfwk_enterprisearchitecture() {
        return contentfwk_enterprisearchitecture;
    }

    public void setContentfwk_enterprisearchitecture(contentfwk_EnterpriseArchitecture contentfwk_enterprisearchitecture) {
        this.contentfwk_enterprisearchitecture = contentfwk_enterprisearchitecture;
    }

}