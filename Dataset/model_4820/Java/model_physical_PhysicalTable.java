





import java.util.List;
import java.util.ArrayList;

public class model_physical_PhysicalTable extends ModelObject {

    private String comment;
    private String type;



    public model_physical_PhysicalTable(
        String comment,        String type    ) {
        super(
        );
        this.comment = comment;
        this.type = type;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}