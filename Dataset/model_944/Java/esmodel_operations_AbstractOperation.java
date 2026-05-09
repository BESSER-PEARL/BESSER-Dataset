




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_AbstractOperation extends IdentifiableElement {

    private String name;
    private LocalDate clientDate;
    private String description;
    private boolean accepted;



    public esmodel_operations_AbstractOperation(
        String name,        LocalDate clientDate,        String description,        boolean accepted    ) {
        super(
        );
        this.name = name;
        this.clientDate = clientDate;
        this.description = description;
        this.accepted = accepted;
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


}