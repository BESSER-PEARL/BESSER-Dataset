





import java.util.List;
import java.util.ArrayList;

public class highlevelnets_common_INetElement extends IEntityIdentifiable {

    private String name;
    private String comment;



    public highlevelnets_common_INetElement(
        String name,        String comment    ) {
        super(
        );
        this.name = name;
        this.comment = comment;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}