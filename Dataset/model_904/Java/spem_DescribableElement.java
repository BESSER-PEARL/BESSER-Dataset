




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class spem_DescribableElement extends ExtensibleElement {

    private String mainDescription;
    private String purpose;
    private String changeDescription;
    private String version;
    private String author;
    private LocalDate changeDate;
    private String presentationName;
    private String copyright;
    private String briefDescription;



    public spem_DescribableElement(
        String mainDescription,        String purpose,        String changeDescription,        String version,        String author,        LocalDate changeDate,        String presentationName,        String copyright,        String briefDescription    ) {
        super(
        );
        this.mainDescription = mainDescription;
        this.purpose = purpose;
        this.changeDescription = changeDescription;
        this.version = version;
        this.author = author;
        this.changeDate = changeDate;
        this.presentationName = presentationName;
        this.copyright = copyright;
        this.briefDescription = briefDescription;
    }


    public String getMaindescription() {
        return mainDescription;
    }

    public void setMaindescription(String mainDescription) {
        this.mainDescription = mainDescription;
    }
    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }
    public String getChangedescription() {
        return changeDescription;
    }

    public void setChangedescription(String changeDescription) {
        this.changeDescription = changeDescription;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public LocalDate getChangedate() {
        return changeDate;
    }

    public void setChangedate(LocalDate changeDate) {
        this.changeDate = changeDate;
    }
    public String getPresentationname() {
        return presentationName;
    }

    public void setPresentationname(String presentationName) {
        this.presentationName = presentationName;
    }
    public String getCopyright() {
        return copyright;
    }

    public void setCopyright(String copyright) {
        this.copyright = copyright;
    }
    public String getBriefdescription() {
        return briefDescription;
    }

    public void setBriefdescription(String briefDescription) {
        this.briefDescription = briefDescription;
    }


}