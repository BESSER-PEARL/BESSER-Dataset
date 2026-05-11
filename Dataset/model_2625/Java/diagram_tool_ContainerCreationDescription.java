





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_ContainerCreationDescription extends MappingBasedToolDescription {

    private String iconPath;



    public diagram_tool_ContainerCreationDescription(
        String iconPath    ) {
        super(
        );
        this.iconPath = iconPath;
    }


    public String getIconpath() {
        return iconPath;
    }

    public void setIconpath(String iconPath) {
        this.iconPath = iconPath;
    }


}