





import java.util.List;
import java.util.ArrayList;

public class uma_DescribableElement extends MethodElement {

    private String isAbstract;
    private String nodeicon;
    private String shapeicon;
    private String fulfill;



    public uma_DescribableElement(
        String isAbstract,        String nodeicon,        String shapeicon,        String fulfill    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.nodeicon = nodeicon;
        this.shapeicon = shapeicon;
        this.fulfill = fulfill;
    }


    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
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
    public String getFulfill() {
        return fulfill;
    }

    public void setFulfill(String fulfill) {
        this.fulfill = fulfill;
    }


}