





import java.util.List;
import java.util.ArrayList;

public class contentfwk_ApplicationArchitecture extends Architecture {






    private List<contentfwk_EObject> contentfwk_eobjects;


    public contentfwk_ApplicationArchitecture(
    ) {
        super(
        );
        this.contentfwk_eobjects = new ArrayList<>();
    }

    public contentfwk_ApplicationArchitecture(
        ArrayList<contentfwk_EObject> contentfwk_eobjects    ) {
        this.contentfwk_eobjects = contentfwk_eobjects;
    }


    public List<contentfwk_EObject> getContentfwk_eobjects() {
        return contentfwk_eobjects;
    }

    public void addContentfwk_eobject(Contentfwk_eobject contentfwk_eobject) {
        this.contentfwk_eobjects.add(contentfwk_eobject);
    }

}