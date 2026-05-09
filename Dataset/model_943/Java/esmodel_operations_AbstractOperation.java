




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_AbstractOperation extends IdentifiableElement {

    private String description;
    private boolean accepted;
    private LocalDate clientDate;
    private String name;



    public esmodel_operations_AbstractOperation(
        String description,        boolean accepted,        LocalDate clientDate,        String name    ) {
        super(
        );
        this.description = description;
        this.accepted = accepted;
        this.clientDate = clientDate;
        this.name = name;
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
    public LocalDate getClientdate() {
        return clientDate;
    }

    public void setClientdate(LocalDate clientDate) {
        this.clientDate = clientDate;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}