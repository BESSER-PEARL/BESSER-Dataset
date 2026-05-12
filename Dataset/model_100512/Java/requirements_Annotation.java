




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class requirements_Annotation  {

    private String annotation;
    private String id;
    private String comment;
    private LocalDate date;
    private String author;
    private String status;





    private requirements_AnnotableElement requirements_annotableelement;


    public requirements_Annotation(
        String annotation,        String id,        String comment,        LocalDate date,        String author,        String status    ) {
        this.annotation = annotation;
        this.id = id;
        this.comment = comment;
        this.date = date;
        this.author = author;
        this.status = status;
    }


    public String getAnnotation() {
        return annotation;
    }

    public void setAnnotation(String annotation) {
        this.annotation = annotation;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public requirements_AnnotableElement getRequirements_annotableelement() {
        return requirements_annotableelement;
    }

    public void setRequirements_annotableelement(requirements_AnnotableElement requirements_annotableelement) {
        this.requirements_annotableelement = requirements_annotableelement;
    }

}