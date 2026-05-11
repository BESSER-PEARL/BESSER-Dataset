





import java.util.List;
import java.util.ArrayList;

public class attributes_DocumentRoot  {

    private String comment;
    private String mixed;



    public attributes_DocumentRoot(
        String comment,        String mixed    ) {
        this.comment = comment;
        this.mixed = mixed;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }


}