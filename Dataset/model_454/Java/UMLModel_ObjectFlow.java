





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ObjectFlow extends ActivityEdge {

    private String transformation;
    private String isMultireceive;
    private String selection;
    private String isMulticast;



    public UMLModel_ObjectFlow(
        String transformation,        String isMultireceive,        String selection,        String isMulticast    ) {
        super(
        );
        this.transformation = transformation;
        this.isMultireceive = isMultireceive;
        this.selection = selection;
        this.isMulticast = isMulticast;
    }


    public String getTransformation() {
        return transformation;
    }

    public void setTransformation(String transformation) {
        this.transformation = transformation;
    }
    public String getIsmultireceive() {
        return isMultireceive;
    }

    public void setIsmultireceive(String isMultireceive) {
        this.isMultireceive = isMultireceive;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }
    public String getIsmulticast() {
        return isMulticast;
    }

    public void setIsmulticast(String isMulticast) {
        this.isMulticast = isMulticast;
    }


}