





import java.util.List;
import java.util.ArrayList;

public class aredsl_Action  {

    private String description;





    private aredsl_Tool aredsl_tool;


    public aredsl_Action(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public aredsl_Tool getAredsl_tool() {
        return aredsl_tool;
    }

    public void setAredsl_tool(aredsl_Tool aredsl_tool) {
        this.aredsl_tool = aredsl_tool;
    }

}