





import java.util.List;
import java.util.ArrayList;

public class uma_DescribableElement extends MethodElement {

    private String isAbstract;
    private String fulfill;
    private String nodeicon;
    private String shapeicon;



    public uma_DescribableElement(
        String isAbstract,        String fulfill,        String nodeicon,        String shapeicon    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.fulfill = fulfill;
        this.nodeicon = nodeicon;
        this.shapeicon = shapeicon;
    }


    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getFulfill() {
        return fulfill;
    }

    public void setFulfill(String fulfill) {
        this.fulfill = fulfill;
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