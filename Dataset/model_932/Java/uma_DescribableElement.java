





import java.util.List;
import java.util.ArrayList;

public class uma_DescribableElement extends MethodElement, Classifier {

    private String nodeicon;
    private String shapeicon;
    private String presentationName;





    private uma_ContentDescription uma_contentdescription;


    public uma_DescribableElement(
        String nodeicon,        String shapeicon,        String presentationName    ) {
        super(
        );
        this.nodeicon = nodeicon;
        this.shapeicon = shapeicon;
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
    public String getPresentationname() {
        return presentationName;
    }

    public void setPresentationname(String presentationName) {
        this.presentationName = presentationName;
    }

    public uma_ContentDescription getUma_contentdescription() {
        return uma_contentdescription;
    }

    public void setUma_contentdescription(uma_ContentDescription uma_contentdescription) {
        this.uma_contentdescription = uma_contentdescription;
    }

}