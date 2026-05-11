





import java.util.List;
import java.util.ArrayList;

public class qm_DescribedElement extends AnnotatedElement {

    private String description;



    public qm_DescribedElement(
        String description    ) {
        super(
        );
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}