




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class lobj_CourseMeta extends LearningObject {

    private int hours;
    private String lvanr;
    private String fromext;
    private String columnfilterasxml;
    private LocalDate creationDate;





    private lobj_Language lobj_language;


    public lobj_CourseMeta(
        int hours,        String lvanr,        String fromext,        String columnfilterasxml,        LocalDate creationDate    ) {
        super(
        );
        this.hours = hours;
        this.lvanr = lvanr;
        this.fromext = fromext;
        this.columnfilterasxml = columnfilterasxml;
        this.creationDate = creationDate;
    }


    public int getHours() {
        return hours;
    }

    public void setHours(int hours) {
        this.hours = hours;
    }
    public String getLvanr() {
        return lvanr;
    }

    public void setLvanr(String lvanr) {
        this.lvanr = lvanr;
    }
    public String getFromext() {
        return fromext;
    }

    public void setFromext(String fromext) {
        this.fromext = fromext;
    }
    public String getColumnfilterasxml() {
        return columnfilterasxml;
    }

    public void setColumnfilterasxml(String columnfilterasxml) {
        this.columnfilterasxml = columnfilterasxml;
    }
    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }

    public lobj_Language getLobj_language() {
        return lobj_language;
    }

    public void setLobj_language(lobj_Language lobj_language) {
        this.lobj_language = lobj_language;
    }

}