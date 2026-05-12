





import java.util.List;
import java.util.ArrayList;

public class styles_StyleContainerElement  {

    private String name;
    private String description;





    private styles_StyleContainer styles_stylecontainer;


    public styles_StyleContainerElement(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public styles_StyleContainer getStyles_stylecontainer() {
        return styles_stylecontainer;
    }

    public void setStyles_stylecontainer(styles_StyleContainer styles_stylecontainer) {
        this.styles_stylecontainer = styles_stylecontainer;
    }

}