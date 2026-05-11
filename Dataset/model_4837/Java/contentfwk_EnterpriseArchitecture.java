





import java.util.List;
import java.util.ArrayList;

public class contentfwk_EnterpriseArchitecture  {






    private List<contentfwk_Container> contentfwk_containers;


    public contentfwk_EnterpriseArchitecture(
    ) {
        this.contentfwk_containers = new ArrayList<>();
    }

    public contentfwk_EnterpriseArchitecture(
        ArrayList<contentfwk_Container> contentfwk_containers    ) {
        this.contentfwk_containers = contentfwk_containers;
    }


    public List<contentfwk_Container> getContentfwk_containers() {
        return contentfwk_containers;
    }

    public void addContentfwk_container(Contentfwk_container contentfwk_container) {
        this.contentfwk_containers.add(contentfwk_container);
    }

}