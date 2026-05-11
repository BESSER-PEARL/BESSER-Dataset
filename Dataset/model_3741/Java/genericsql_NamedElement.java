





import java.util.List;
import java.util.ArrayList;

public class genericsql_NamedElement  {

    private String comment;
    private String name;



    public genericsql_NamedElement(
        String comment,        String name    ) {
        this.comment = comment;
        this.name = name;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}