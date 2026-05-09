





import java.util.List;
import java.util.ArrayList;

public class library_TextAnnotation extends Bookmark {

    private String color;
    private String comment;



    public library_TextAnnotation(
        String color,        String comment    ) {
        super(
        );
        this.color = color;
        this.comment = comment;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}