





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Container  {

    private String name;





    private contentfwk_EnterpriseArchitecture contentfwk_enterprisearchitecture;


    public contentfwk_Container(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public contentfwk_EnterpriseArchitecture getContentfwk_enterprisearchitecture() {
        return contentfwk_enterprisearchitecture;
    }

    public void setContentfwk_enterprisearchitecture(contentfwk_EnterpriseArchitecture contentfwk_enterprisearchitecture) {
        this.contentfwk_enterprisearchitecture = contentfwk_enterprisearchitecture;
    }

}