




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class spem_DescribableElement extends ExtensibleElement {

    private String purpose;
    private String presentationName;
    private String version;
    private String briefDescription;
    private String changeDescription;
    private String mainDescription;
    private String copyright;
    private String author;
    private LocalDate changeDate;



    public spem_DescribableElement(
        String purpose,        String presentationName,        String version,        String briefDescription,        String changeDescription,        String mainDescription,        String copyright,        String author,        LocalDate changeDate    ) {
        super(
        );
        this.purpose = purpose;
        this.presentationName = presentationName;
        this.version = version;
        this.briefDescription = briefDescription;
        this.changeDescription = changeDescription;
        this.mainDescription = mainDescription;
        this.copyright = copyright;
        this.author = author;
        this.changeDate = changeDate;
    }


    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }
    public String getPresentationname() {
        return presentationName;
    }

    public void setPresentationname(String presentationName) {
        this.presentationName = presentationName;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getBriefdescription() {
        return briefDescription;
    }

    public void setBriefdescription(String briefDescription) {
        this.briefDescription = briefDescription;
    }
    public String getChangedescription() {
        return changeDescription;
    }

    public void setChangedescription(String changeDescription) {
        this.changeDescription = changeDescription;
    }
    public String getMaindescription() {
        return mainDescription;
    }

    public void setMaindescription(String mainDescription) {
        this.mainDescription = mainDescription;
    }
    public String getCopyright() {
        return copyright;
    }

    public void setCopyright(String copyright) {
        this.copyright = copyright;
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


}