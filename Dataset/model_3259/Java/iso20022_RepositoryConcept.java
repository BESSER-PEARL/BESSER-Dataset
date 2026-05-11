




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class iso20022_RepositoryConcept extends ModelEntity {

    private String example;
    private String name;
    private String registrationStatus;
    private LocalDate removalDate;
    private String definition;



    public iso20022_RepositoryConcept(
        String example,        String name,        String registrationStatus,        LocalDate removalDate,        String definition    ) {
        super(
        );
        this.example = example;
        this.name = name;
        this.registrationStatus = registrationStatus;
        this.removalDate = removalDate;
        this.definition = definition;
    }


    public String getExample() {
        return example;
    }

    public void setExample(String example) {
        this.example = example;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRegistrationstatus() {
        return registrationStatus;
    }

    public void setRegistrationstatus(String registrationStatus) {
        this.registrationStatus = registrationStatus;
    }
    public LocalDate getRemovaldate() {
        return removalDate;
    }

    public void setRemovaldate(LocalDate removalDate) {
        this.removalDate = removalDate;
    }
    public String getDefinition() {
        return definition;
    }

    public void setDefinition(String definition) {
        this.definition = definition;
    }


}