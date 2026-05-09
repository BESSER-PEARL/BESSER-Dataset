




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_AbstractOperation extends IdentifiableElement {

    private String name;
    private LocalDate clientDate;
    private boolean accepted;
    private String description;



    public esmodel_operations_AbstractOperation(
        String name,        LocalDate clientDate,        boolean accepted,        String description    ) {
        super(
        );
        this.name = name;
        this.clientDate = clientDate;
        this.accepted = accepted;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getClientdate() {
        return clientDate;
    }

    public void setClientdate(LocalDate clientDate) {
        this.clientDate = clientDate;
    }
    public boolean getAccepted() {
        return accepted;
    }

    public void setAccepted(boolean accepted) {
        this.accepted = accepted;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}