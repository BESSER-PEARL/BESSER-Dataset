





import java.util.List;
import java.util.ArrayList;

public class qm_NamedElement extends DescribedElement {

    private String title;
    private String name;



    public qm_NamedElement(
        String title,        String name    ) {
        super(
        );
        this.title = title;
        this.name = name;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}