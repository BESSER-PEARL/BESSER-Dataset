





import java.util.List;
import java.util.ArrayList;

public class robot_NamedElement  {

    private String name;
    private String literal;
    private String comment;



    public robot_NamedElement(
        String name,        String literal,        String comment    ) {
        this.name = name;
        this.literal = literal;
        this.comment = comment;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}