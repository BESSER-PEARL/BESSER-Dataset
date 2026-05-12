




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class requirements_Annotation  {

    private String annotation;
    private String status;
    private String author;
    private String id;
    private LocalDate date;
    private String comment;



    public requirements_Annotation(
        String annotation,        String status,        String author,        String id,        LocalDate date,        String comment    ) {
        this.annotation = annotation;
        this.status = status;
        this.author = author;
        this.id = id;
        this.date = date;
        this.comment = comment;
    }


    public String getAnnotation() {
        return annotation;
    }

    public void setAnnotation(String annotation) {
        this.annotation = annotation;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}