





import java.util.List;
import java.util.ArrayList;

public class uma_DescribableElement extends Classifier, MethodElement {

    private String nodeicon;
    private String shapeicon;



    public uma_DescribableElement(
        String nodeicon,        String shapeicon    ) {
        super(
        );
        this.nodeicon = nodeicon;
        this.shapeicon = shapeicon;
    }


    public String getNodeicon() {
        return nodeicon;
    }

    public void setNodeicon(String nodeicon) {
        this.nodeicon = nodeicon;
    }
    public String getShapeicon() {
        return shapeicon;
    }

    public void setShapeicon(String shapeicon) {
        this.shapeicon = shapeicon;
    }


}