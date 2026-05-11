




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class iso20022_RepositoryConcept extends ModelEntity {

    private String example;
    private String name;
    private LocalDate removalDate;
    private String definition;
    private String registrationStatus;





    private List<iso20022_Doclet> iso20022_doclets;




    private List<iso20022_SemanticMarkup> iso20022_semanticmarkups;


    public iso20022_RepositoryConcept(
        String example,        String name,        LocalDate removalDate,        String definition,        String registrationStatus    ) {
        super(
        );
        this.example = example;
        this.name = name;
        this.removalDate = removalDate;
        this.definition = definition;
        this.registrationStatus = registrationStatus;
        this.iso20022_doclets = new ArrayList<>();
        this.iso20022_semanticmarkups = new ArrayList<>();
    }

    public iso20022_RepositoryConcept(
        String example,        String name,        LocalDate removalDate,        String definition,        String registrationStatus        ArrayList<iso20022_Doclet> iso20022_doclets,        ArrayList<iso20022_SemanticMarkup> iso20022_semanticmarkups    ) {
        this.example = example;
        this.name = name;
        this.removalDate = removalDate;
        this.definition = definition;
        this.registrationStatus = registrationStatus;
        this.iso20022_doclets = iso20022_doclets;
        this.iso20022_semanticmarkups = iso20022_semanticmarkups;
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
    public String getRegistrationstatus() {
        return registrationStatus;
    }

    public void setRegistrationstatus(String registrationStatus) {
        this.registrationStatus = registrationStatus;
    }

    public List<iso20022_Doclet> getIso20022_doclets() {
        return iso20022_doclets;
    }

    public void addIso20022_doclet(Iso20022_doclet iso20022_doclet) {
        this.iso20022_doclets.add(iso20022_doclet);
    }
    public List<iso20022_SemanticMarkup> getIso20022_semanticmarkups() {
        return iso20022_semanticmarkups;
    }

    public void addIso20022_semanticmarkup(Iso20022_semanticmarkup iso20022_semanticmarkup) {
        this.iso20022_semanticmarkups.add(iso20022_semanticmarkup);
    }

}