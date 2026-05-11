





import java.util.List;
import java.util.ArrayList;

public class featureDiagram_Feature extends FeatureElement {

    private String name;
    private boolean selected;



    public featureDiagram_Feature(
        String name,        boolean selected    ) {
        super(
        );
        this.name = name;
        this.selected = selected;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }


}