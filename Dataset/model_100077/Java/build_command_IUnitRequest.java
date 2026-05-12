





import java.util.List;
import java.util.ArrayList;

public class build_command_IUnitRequest  {

    private String name;
    private String range;
    private String nameSpace;



    public build_command_IUnitRequest(
        String name,        String range,        String nameSpace    ) {
        this.name = name;
        this.range = range;
        this.nameSpace = nameSpace;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }
    public String getNamespace() {
        return nameSpace;
    }

    public void setNamespace(String nameSpace) {
        this.nameSpace = nameSpace;
    }


}