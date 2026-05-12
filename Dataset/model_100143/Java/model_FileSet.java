





import java.util.List;
import java.util.ArrayList;

public class model_FileSet extends NamedElement, DescribedElement {

    private String hostname;





    private model_Site model_site;


    public model_FileSet(
        String hostname    ) {
        super(
        );
        this.hostname = hostname;
    }


    public String getHostname() {
        return hostname;
    }

    public void setHostname(String hostname) {
        this.hostname = hostname;
    }

    public model_Site getModel_site() {
        return model_site;
    }

    public void setModel_site(model_Site model_site) {
        this.model_site = model_site;
    }

}