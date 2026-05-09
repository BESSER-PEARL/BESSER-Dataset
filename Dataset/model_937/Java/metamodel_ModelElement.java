




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class metamodel_ModelElement extends IdentifiableElement {

    private LocalDate creationDate;
    private String creator;



    public metamodel_ModelElement(
        LocalDate creationDate,        String creator    ) {
        super(
        );
        this.creationDate = creationDate;
        this.creator = creator;
    }


    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }
    public String getCreator() {
        return creator;
    }

    public void setCreator(String creator) {
        this.creator = creator;
    }


}