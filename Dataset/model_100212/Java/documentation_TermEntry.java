





import java.util.List;
import java.util.ArrayList;

public class documentation_TermEntry extends NamedElement {

    private String description;



    public documentation_TermEntry(
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