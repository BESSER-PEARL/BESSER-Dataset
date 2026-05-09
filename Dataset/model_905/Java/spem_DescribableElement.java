




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class spem_DescribableElement extends ExtensibleElement {

    private String briefDescription;
    private LocalDate changeDate;
    private String author;
    private String changeDescription;
    private String copyright;
    private String version;
    private String presentationName;
    private String mainDescription;
    private String purpose;



    public spem_DescribableElement(
        String briefDescription,        LocalDate changeDate,        String author,        String changeDescription,        String copyright,        String version,        String presentationName,        String mainDescription,        String purpose    ) {
        super(
        );
        this.briefDescription = briefDescription;
        this.changeDate = changeDate;
        this.author = author;
        this.changeDescription = changeDescription;
        this.copyright = copyright;
        this.version = version;
        this.presentationName = presentationName;
        this.mainDescription = mainDescription;
        this.purpose = purpose;
    }


    public String getBriefdescription() {
        return briefDescription;
    }

    public void setBriefdescription(String briefDescription) {
        this.briefDescription = briefDescription;
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
    public String getPresentationname() {
        return presentationName;
    }

    public void setPresentationname(String presentationName) {
        this.presentationName = presentationName;
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


}