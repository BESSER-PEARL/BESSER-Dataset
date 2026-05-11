





import java.util.List;
import java.util.ArrayList;

public class webapp_AbstractView extends NamedElement {

    private String description;



    public webapp_AbstractView(
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