





import java.util.List;
import java.util.ArrayList;

public class uma_DescribableElement extends MethodElement, Classifier {

    private String shapeicon;
    private String nodeicon;



    public uma_DescribableElement(
        String shapeicon,        String nodeicon    ) {
        super(
        );
        this.shapeicon = shapeicon;
        this.nodeicon = nodeicon;
    }


    public String getShapeicon() {
        return shapeicon;
    }

    public void setShapeicon(String shapeicon) {
        this.shapeicon = shapeicon;
    }
    public String getNodeicon() {
        return nodeicon;
    }

    public void setNodeicon(String nodeicon) {
        this.nodeicon = nodeicon;
    }


}