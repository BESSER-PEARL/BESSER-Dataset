




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class metamodel_ModelElement extends IdentifiableElement {

    private String creator;
    private LocalDate creationDate;



    public metamodel_ModelElement(
        String creator,        LocalDate creationDate    ) {
        super(
        );
        this.creator = creator;
        this.creationDate = creationDate;
    }


    public String getCreator() {
        return creator;
    }

    public void setCreator(String creator) {
        this.creator = creator;
    }
    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }


}