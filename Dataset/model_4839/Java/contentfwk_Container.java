





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Container  {

    private String name;
    private String description;
    private String id;





    private contentfwk_EnterpriseArchitecture contentfwk_enterprisearchitecture;




    private contentfwk_Container contentfwk_container;


    public contentfwk_Container(
        String name,        String description,        String id    ) {
        this.name = name;
        this.description = description;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public contentfwk_EnterpriseArchitecture getContentfwk_enterprisearchitecture() {
        return contentfwk_enterprisearchitecture;
    }

    public void setContentfwk_enterprisearchitecture(contentfwk_EnterpriseArchitecture contentfwk_enterprisearchitecture) {
        this.contentfwk_enterprisearchitecture = contentfwk_enterprisearchitecture;
    }
    public contentfwk_Container getContentfwk_container() {
        return contentfwk_container;
    }

    public void setContentfwk_container(contentfwk_Container contentfwk_container) {
        this.contentfwk_container = contentfwk_container;
    }

}