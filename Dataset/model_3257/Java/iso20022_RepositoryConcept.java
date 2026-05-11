




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class iso20022_RepositoryConcept extends ModelEntity {

    private String registrationStatus;
    private String name;
    private LocalDate removalDate;
    private String example;
    private String definition;





    private List<iso20022_SemanticMarkup> iso20022_semanticmarkups;




    private List<iso20022_Doclet> iso20022_doclets;


    public iso20022_RepositoryConcept(
        String registrationStatus,        String name,        LocalDate removalDate,        String example,        String definition    ) {
        super(
        );
        this.registrationStatus = registrationStatus;
        this.name = name;
        this.removalDate = removalDate;
        this.example = example;
        this.definition = definition;
        this.iso20022_semanticmarkups = new ArrayList<>();
        this.iso20022_doclets = new ArrayList<>();
    }

    public iso20022_RepositoryConcept(
        String registrationStatus,        String name,        LocalDate removalDate,        String example,        String definition        ArrayList<iso20022_SemanticMarkup> iso20022_semanticmarkups,        ArrayList<iso20022_Doclet> iso20022_doclets    ) {
        this.registrationStatus = registrationStatus;
        this.name = name;
        this.removalDate = removalDate;
        this.example = example;
        this.definition = definition;
        this.iso20022_semanticmarkups = iso20022_semanticmarkups;
        this.iso20022_doclets = iso20022_doclets;
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
    public String getDefinition() {
        return definition;
    }

    public void setDefinition(String definition) {
        this.definition = definition;
    }

    public List<iso20022_SemanticMarkup> getIso20022_semanticmarkups() {
        return iso20022_semanticmarkups;
    }

    public void addIso20022_semanticmarkup(Iso20022_semanticmarkup iso20022_semanticmarkup) {
        this.iso20022_semanticmarkups.add(iso20022_semanticmarkup);
    }
    public List<iso20022_Doclet> getIso20022_doclets() {
        return iso20022_doclets;
    }

    public void addIso20022_doclet(Iso20022_doclet iso20022_doclet) {
        this.iso20022_doclets.add(iso20022_doclet);
    }

}