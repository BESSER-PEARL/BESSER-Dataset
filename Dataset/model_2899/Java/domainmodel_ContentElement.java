





import java.util.List;
import java.util.ArrayList;

public class domainmodel_ContentElement extends ViewElement {

    private String contentElement;



    public domainmodel_ContentElement(
        String contentElement    ) {
        super(
        );
        this.contentElement = contentElement;
    }


    public String getContentelement() {
        return contentElement;
    }

    public void setContentelement(String contentElement) {
        this.contentElement = contentElement;
    }


}