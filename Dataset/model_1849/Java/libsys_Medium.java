




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class libsys_Medium  {

    private String partialShelfmark;
    private String identificationCode;
    private String authors;
    private String title;
    private String keywords;
    private LocalDate publicationYear;
    private String additionalTitle;



    public libsys_Medium(
        String partialShelfmark,        String identificationCode,        String authors,        String title,        String keywords,        LocalDate publicationYear,        String additionalTitle    ) {
        this.partialShelfmark = partialShelfmark;
        this.identificationCode = identificationCode;
        this.authors = authors;
        this.title = title;
        this.keywords = keywords;
        this.publicationYear = publicationYear;
        this.additionalTitle = additionalTitle;
    }


    public String getPartialshelfmark() {
        return partialShelfmark;
    }

    public void setPartialshelfmark(String partialShelfmark) {
        this.partialShelfmark = partialShelfmark;
    }
    public String getIdentificationcode() {
        return identificationCode;
    }

    public void setIdentificationcode(String identificationCode) {
        this.identificationCode = identificationCode;
    }
    public String getAuthors() {
        return authors;
    }

    public void setAuthors(String authors) {
        this.authors = authors;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getKeywords() {
        return keywords;
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
    }
    public LocalDate getPublicationyear() {
        return publicationYear;
    }

    public void setPublicationyear(LocalDate publicationYear) {
        this.publicationYear = publicationYear;
    }
    public String getAdditionaltitle() {
        return additionalTitle;
    }

    public void setAdditionaltitle(String additionalTitle) {
        this.additionalTitle = additionalTitle;
    }


}