





import java.util.List;
import java.util.ArrayList;

public class fc_AttributeValue  {

    private String name;
    private String comment;
    private String description;
    private String id;





    private fc_Selection fc_selection;




    private fc_Selection fc_selection;


    public fc_AttributeValue(
        String name,        String comment,        String description,        String id    ) {
        this.name = name;
        this.comment = comment;
        this.description = description;
        this.id = id;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public fc_Selection getFc_selection() {
        return fc_selection;
    }

    public void setFc_selection(fc_Selection fc_selection) {
        this.fc_selection = fc_selection;
    }
    public fc_Selection getFc_selection() {
        return fc_selection;
    }

    public void setFc_selection(fc_Selection fc_selection) {
        this.fc_selection = fc_selection;
    }

}