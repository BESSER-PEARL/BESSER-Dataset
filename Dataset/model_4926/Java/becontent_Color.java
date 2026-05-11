





import java.util.List;
import java.util.ArrayList;

public class becontent_Color extends NotStructuredElement {

    private String label;
    private String name;
    private String defaultColor;



    public becontent_Color(
        String label,        String name,        String defaultColor    ) {
        super(
        );
        this.label = label;
        this.name = name;
        this.defaultColor = defaultColor;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDefaultcolor() {
        return defaultColor;
    }

    public void setDefaultcolor(String defaultColor) {
        this.defaultColor = defaultColor;
    }


}