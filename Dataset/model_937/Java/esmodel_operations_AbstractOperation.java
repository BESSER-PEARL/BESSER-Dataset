




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_AbstractOperation extends IdentifiableElement {

    private LocalDate clientDate;
    private String description;
    private boolean accepted;
    private String name;





    private ModelElementId modelelementid;


    public esmodel_operations_AbstractOperation(
        LocalDate clientDate,        String description,        boolean accepted,        String name    ) {
        super(
        );
        this.clientDate = clientDate;
        this.description = description;
        this.accepted = accepted;
        this.name = name;
    }


    public LocalDate getClientdate() {
        return clientDate;
    }

    public void setClientdate(LocalDate clientDate) {
        this.clientDate = clientDate;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public boolean getAccepted() {
        return accepted;
    }

    public void setAccepted(boolean accepted) {
        this.accepted = accepted;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ModelElementId getModelelementid() {
        return modelelementid;
    }

    public void setModelelementid(ModelElementId modelelementid) {
        this.modelelementid = modelelementid;
    }

}