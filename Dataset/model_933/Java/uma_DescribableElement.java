





import java.util.List;
import java.util.ArrayList;

public class uma_DescribableElement extends MethodElement {

    private String nodeicon;
    private String fulfill;
    private String isAbstract;
    private String shapeicon;



    public uma_DescribableElement(
        String nodeicon,        String fulfill,        String isAbstract,        String shapeicon    ) {
        super(
        );
        this.nodeicon = nodeicon;
        this.fulfill = fulfill;
        this.isAbstract = isAbstract;
        this.shapeicon = shapeicon;
    }


    public String getNodeicon() {
        return nodeicon;
    }

    public void setNodeicon(String nodeicon) {
        this.nodeicon = nodeicon;
    }
    public String getFulfill() {
        return fulfill;
    }

    public void setFulfill(String fulfill) {
        this.fulfill = fulfill;
    }
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getShapeicon() {
        return shapeicon;
    }

    public void setShapeicon(String shapeicon) {
        this.shapeicon = shapeicon;
    }


}