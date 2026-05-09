




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class spem_MethodContentElement extends DescribableElement, MethodContentPackageableElement, VariabilityElement {

    private String copyright;
    private String version;
    private LocalDate changeDate;
    private String author;
    private String changeDescription;





    private spem_MethodContentElement spem_methodcontentelement;


    public spem_MethodContentElement(
        String copyright,        String version,        LocalDate changeDate,        String author,        String changeDescription    ) {
        super(
        );
        this.copyright = copyright;
        this.version = version;
        this.changeDate = changeDate;
        this.author = author;
        this.changeDescription = changeDescription;
    }


    public String getCopyright() {
        return copyright;
    }

    public void setCopyright(String copyright) {
        this.copyright = copyright;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public LocalDate getChangedate() {
        return changeDate;
    }

    public void setChangedate(LocalDate changeDate) {
        this.changeDate = changeDate;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getChangedescription() {
        return changeDescription;
    }

    public void setChangedescription(String changeDescription) {
        this.changeDescription = changeDescription;
    }

    public spem_MethodContentElement getSpem_methodcontentelement() {
        return spem_methodcontentelement;
    }

    public void setSpem_methodcontentelement(spem_MethodContentElement spem_methodcontentelement) {
        this.spem_methodcontentelement = spem_methodcontentelement;
    }

}