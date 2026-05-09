




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_AbstractOperation extends IdentifiableElement {

    private String description;
    private LocalDate clientDate;
    private String name;
    private boolean accepted;



    public esmodel_operations_AbstractOperation(
        String description,        LocalDate clientDate,        String name,        boolean accepted    ) {
        super(
        );
        this.description = description;
        this.clientDate = clientDate;
        this.name = name;
        this.accepted = accepted;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getAccepted() {
        return accepted;
    }

    public void setAccepted(boolean accepted) {
        this.accepted = accepted;
    }


}