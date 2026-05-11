





import java.util.List;
import java.util.ArrayList;

public class architectureTool_Attribute  {

    private String type;
    private String name;
    private String Visable;



    public architectureTool_Attribute(
        String type,        String name,        String Visable    ) {
        this.type = type;
        this.name = name;
        this.Visable = Visable;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVisable() {
        return Visable;
    }

    public void setVisable(String Visable) {
        this.Visable = Visable;
    }


}