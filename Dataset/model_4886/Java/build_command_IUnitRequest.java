





import java.util.List;
import java.util.ArrayList;

public class build_command_IUnitRequest  {

    private String name;
    private String nameSpace;
    private String range;



    public build_command_IUnitRequest(
        String name,        String nameSpace,        String range    ) {
        this.name = name;
        this.nameSpace = nameSpace;
        this.range = range;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNamespace() {
        return nameSpace;
    }

    public void setNamespace(String nameSpace) {
        this.nameSpace = nameSpace;
    }
    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }


}