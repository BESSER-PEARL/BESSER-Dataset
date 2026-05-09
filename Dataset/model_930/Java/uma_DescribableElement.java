





import java.util.List;
import java.util.ArrayList;

public class uma_DescribableElement extends Classifier, MethodElement {

    private String nodeicon;
    private String presentationName;
    private String shapeicon;





    private uma_CustomCategory uma_customcategory;


    public uma_DescribableElement(
        String nodeicon,        String presentationName,        String shapeicon    ) {
        super(
        );
        this.nodeicon = nodeicon;
        this.presentationName = presentationName;
        this.shapeicon = shapeicon;
    }


    public String getNodeicon() {
        return nodeicon;
    }

    public void setNodeicon(String nodeicon) {
        this.nodeicon = nodeicon;
    }
    public String getPresentationname() {
        return presentationName;
    }

    public void setPresentationname(String presentationName) {
        this.presentationName = presentationName;
    }
    public String getShapeicon() {
        return shapeicon;
    }

    public void setShapeicon(String shapeicon) {
        this.shapeicon = shapeicon;
    }

    public uma_CustomCategory getUma_customcategory() {
        return uma_customcategory;
    }

    public void setUma_customcategory(uma_CustomCategory uma_customcategory) {
        this.uma_customcategory = uma_customcategory;
    }

}