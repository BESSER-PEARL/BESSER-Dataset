




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class spem_DescribableElement extends ExtensibleElement {

    private LocalDate changeDate;
    private String purpose;
    private String presentationName;
    private String changeDescription;
    private String mainDescription;
    private String briefDescription;
    private String author;
    private String version;
    private String copyright;



    public spem_DescribableElement(
        LocalDate changeDate,        String purpose,        String presentationName,        String changeDescription,        String mainDescription,        String briefDescription,        String author,        String version,        String copyright    ) {
        super(
        );
        this.changeDate = changeDate;
        this.purpose = purpose;
        this.presentationName = presentationName;
        this.changeDescription = changeDescription;
        this.mainDescription = mainDescription;
        this.briefDescription = briefDescription;
        this.author = author;
        this.version = version;
        this.copyright = copyright;
    }


    public LocalDate getChangedate() {
        return changeDate;
    }

    public void setChangedate(LocalDate changeDate) {
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
    public String getBriefdescription() {
        return briefDescription;
    }

    public void setBriefdescription(String briefDescription) {
        this.briefDescription = briefDescription;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getCopyright() {
        return copyright;
    }

    public void setCopyright(String copyright) {
        this.copyright = copyright;
    }


}