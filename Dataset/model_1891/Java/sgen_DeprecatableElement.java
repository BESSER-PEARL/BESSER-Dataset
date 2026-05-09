





import java.util.List;
import java.util.ArrayList;

public class sgen_DeprecatableElement  {

    private String comment;
    private boolean deprecated;



    public sgen_DeprecatableElement(
        String comment,        boolean deprecated    ) {
        this.comment = comment;
        this.deprecated = deprecated;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public boolean getDeprecated() {
        return deprecated;
    }

    public void setDeprecated(boolean deprecated) {
        this.deprecated = deprecated;
    }


}