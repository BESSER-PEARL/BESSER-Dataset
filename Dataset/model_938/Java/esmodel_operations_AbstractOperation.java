




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_AbstractOperation extends IdentifiableElement {

    private boolean accepted;
    private String name;
    private String description;
    private LocalDate clientDate;



    public esmodel_operations_AbstractOperation(
        boolean accepted,        String name,        String description,        LocalDate clientDate    ) {
        super(
        );
        this.accepted = accepted;
        this.name = name;
        this.description = description;
        this.clientDate = clientDate;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public LocalDate getClientdate() {
        return clientDate;
    }

    public void setClientdate(LocalDate clientDate) {
        this.clientDate = clientDate;
    }


}