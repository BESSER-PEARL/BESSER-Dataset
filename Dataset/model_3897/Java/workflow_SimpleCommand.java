





import java.util.List;
import java.util.ArrayList;

public class workflow_SimpleCommand extends Statement {

    private String description;



    public workflow_SimpleCommand(
        String description    ) {
        super(
        );
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}