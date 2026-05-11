





import java.util.List;
import java.util.ArrayList;

public class activity_ObjectFlow extends ActivityEdge {

    private boolean isMultireceive;
    private boolean isMulticast;



    public activity_ObjectFlow(
        boolean isMultireceive,        boolean isMulticast    ) {
        super(
        );
        this.isMultireceive = isMultireceive;
        this.isMulticast = isMulticast;
    }


    public boolean getIsmultireceive() {
        return isMultireceive;
    }

    public void setIsmultireceive(boolean isMultireceive) {
        this.isMultireceive = isMultireceive;
    }
    public boolean getIsmulticast() {
        return isMulticast;
    }

    public void setIsmulticast(boolean isMulticast) {
        this.isMulticast = isMulticast;
    }


}