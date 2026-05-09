





import java.util.List;
import java.util.ArrayList;

public class uma_DescribableElement extends MethodElement {

    private String shapeicon;
    private String isAbstract;
    private String fulfill;
    private String nodeicon;



    public uma_DescribableElement(
        String shapeicon,        String isAbstract,        String fulfill,        String nodeicon    ) {
        super(
        );
        this.shapeicon = shapeicon;
        this.isAbstract = isAbstract;
        this.fulfill = fulfill;
        this.nodeicon = nodeicon;
    }


    public String getShapeicon() {
        return shapeicon;
    }

    public void setShapeicon(String shapeicon) {
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


}