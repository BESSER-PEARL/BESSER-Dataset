




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ISO20022_RepositoryConcept extends ModelEntity {

    private String definition;
    private LocalDate swiftRemovalDate;
    private LocalDate removalDate;
    private String example;
    private String registrationStatus;
    private String name;
    private String swiftRegistrationStatus;





    private ISO20022_Constraint iso20022_constraint;




    private List<ISO20022_Constraint> iso20022_constraints;


    public ISO20022_RepositoryConcept(
        String definition,        LocalDate swiftRemovalDate,        LocalDate removalDate,        String example,        String registrationStatus,        String name,        String swiftRegistrationStatus    ) {
        super(
        );
        this.definition = definition;
        this.swiftRemovalDate = swiftRemovalDate;
        this.removalDate = removalDate;
        this.example = example;
        this.registrationStatus = registrationStatus;
        this.name = name;
        this.swiftRegistrationStatus = swiftRegistrationStatus;
        this.iso20022_constraints = new ArrayList<>();
    }

    public ISO20022_RepositoryConcept(
        String definition,        LocalDate swiftRemovalDate,        LocalDate removalDate,        String example,        String registrationStatus,        String name,        String swiftRegistrationStatus        ArrayList<ISO20022_Constraint> iso20022_constraints    ) {
        this.definition = definition;
        this.swiftRemovalDate = swiftRemovalDate;
        this.removalDate = removalDate;
        this.example = example;
        this.registrationStatus = registrationStatus;
        this.name = name;
        this.swiftRegistrationStatus = swiftRegistrationStatus;
        this.iso20022_constraints = iso20022_constraints;
    }

    public String getDefinition() {
        return definition;
    }

    public void setDefinition(String definition) {
        this.definition = definition;
    }
    public LocalDate getSwiftremovaldate() {
        return swiftRemovalDate;
    }

    public void setSwiftremovaldate(LocalDate swiftRemovalDate) {
        this.swiftRemovalDate = swiftRemovalDate;
    }
    public LocalDate getRemovaldate() {
        return removalDate;
    }

    public void setRemovaldate(LocalDate removalDate) {
        this.removalDate = removalDate;
    }
    public String getExample() {
        return example;
    }

    public void setExample(String example) {
        this.example = example;
    }
    public String getRegistrationstatus() {
        return registrationStatus;
    }

    public void setRegistrationstatus(String registrationStatus) {
        this.registrationStatus = registrationStatus;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSwiftregistrationstatus() {
        return swiftRegistrationStatus;
    }

    public void setSwiftregistrationstatus(String swiftRegistrationStatus) {
        this.swiftRegistrationStatus = swiftRegistrationStatus;
    }

    public ISO20022_Constraint getIso20022_constraint() {
        return iso20022_constraint;
    }

    public void setIso20022_constraint(ISO20022_Constraint iso20022_constraint) {
        this.iso20022_constraint = iso20022_constraint;
    }
    public List<ISO20022_Constraint> getIso20022_constraints() {
        return iso20022_constraints;
    }

    public void addIso20022_constraint(Iso20022_constraint iso20022_constraint) {
        this.iso20022_constraints.add(iso20022_constraint);
    }

}