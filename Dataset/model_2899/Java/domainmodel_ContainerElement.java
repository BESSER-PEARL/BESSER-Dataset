





import java.util.List;
import java.util.ArrayList;

public class domainmodel_ContainerElement extends ViewElement {

    private String container;



    public domainmodel_ContainerElement(
        String container    ) {
        super(
        );
        this.container = container;
    }


    public String getContainer() {
        return container;
    }

    public void setContainer(String container) {
        this.container = container;
    }


}