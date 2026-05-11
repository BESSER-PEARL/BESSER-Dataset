





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelArchimateObject extends TextPosition, DiagramModelObject, DiagramModelContainer, DiagramModelArchimateComponent {

    private int type;



    public model_DiagramModelArchimateObject(
        int type    ) {
        super(
        );
        this.type = type;
    }


    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }


}