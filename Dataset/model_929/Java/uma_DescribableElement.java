





import java.util.List;
import java.util.ArrayList;

public class uma_DescribableElement extends MethodElement, Classifier {

    private String presentationName;
    private String nodeicon;
    private String shapeicon;



    public uma_DescribableElement(
        String presentationName,        String nodeicon,        String shapeicon    ) {
        super(
        );
        this.presentationName = presentationName;
        this.nodeicon = nodeicon;
        this.shapeicon = shapeicon;
    }


    public String getPresentationname() {
        return presentationName;
    }

    public void setPresentationname(String presentationName) {
        this.presentationName = presentationName;
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