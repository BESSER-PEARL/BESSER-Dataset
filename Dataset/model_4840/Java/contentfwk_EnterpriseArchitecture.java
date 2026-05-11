





import java.util.List;
import java.util.ArrayList;

public class contentfwk_EnterpriseArchitecture  {






    private List<contentfwk_Label> contentfwk_labels;




    private List<contentfwk_Architecture> contentfwk_architectures;




    private List<contentfwk_Container> contentfwk_containers;


    public contentfwk_EnterpriseArchitecture(
    ) {
        this.contentfwk_labels = new ArrayList<>();
        this.contentfwk_architectures = new ArrayList<>();
        this.contentfwk_containers = new ArrayList<>();
    }

    public contentfwk_EnterpriseArchitecture(
        ArrayList<contentfwk_Label> contentfwk_labels,        ArrayList<contentfwk_Architecture> contentfwk_architectures,        ArrayList<contentfwk_Container> contentfwk_containers    ) {
        this.contentfwk_labels = contentfwk_labels;
        this.contentfwk_architectures = contentfwk_architectures;
        this.contentfwk_containers = contentfwk_containers;
    }


    public List<contentfwk_Label> getContentfwk_labels() {
        return contentfwk_labels;
    }

    public void addContentfwk_label(Contentfwk_label contentfwk_label) {
        this.contentfwk_labels.add(contentfwk_label);
    }
    public List<contentfwk_Architecture> getContentfwk_architectures() {
        return contentfwk_architectures;
    }

    public void addContentfwk_architecture(Contentfwk_architecture contentfwk_architecture) {
        this.contentfwk_architectures.add(contentfwk_architecture);
    }
    public List<contentfwk_Container> getContentfwk_containers() {
        return contentfwk_containers;
    }

    public void addContentfwk_container(Contentfwk_container contentfwk_container) {
        this.contentfwk_containers.add(contentfwk_container);
    }

}