




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class BZ_BZEvent  {

    private int issueId;
    private LocalDate date;
    private String oldValue;
    private String field;
    private String newValue;
    private String author;





    private BZ_BZIssue bz_bzissue;




    private BZ_BZIssue bz_bzissue;


    public BZ_BZEvent(
        int issueId,        LocalDate date,        String oldValue,        String field,        String newValue,        String author    ) {
        this.issueId = issueId;
        this.date = date;
        this.oldValue = oldValue;
        this.field = field;
        this.newValue = newValue;
        this.author = author;
    }


    public int getIssueid() {
        return issueId;
    }

    public void setIssueid(int issueId) {
        this.issueId = issueId;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getOldvalue() {
        return oldValue;
    }

    public void setOldvalue(String oldValue) {
        this.oldValue = oldValue;
    }
    public String getField() {
        return field;
    }

    public void setField(String field) {
        this.field = field;
    }
    public String getNewvalue() {
        return newValue;
    }

    public void setNewvalue(String newValue) {
        this.newValue = newValue;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public BZ_BZIssue getBz_bzissue() {
        return bz_bzissue;
    }

    public void setBz_bzissue(BZ_BZIssue bz_bzissue) {
        this.bz_bzissue = bz_bzissue;
    }
    public BZ_BZIssue getBz_bzissue() {
        return bz_bzissue;
    }

    public void setBz_bzissue(BZ_BZIssue bz_bzissue) {
        this.bz_bzissue = bz_bzissue;
    }

}