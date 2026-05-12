





import java.util.List;
import java.util.ArrayList;

public class documentation_Image extends Fragment, NamedElement {

    private String originalSource;
    private String width;



    public documentation_Image(
        String originalSource,        String width    ) {
        super(
        );
        this.originalSource = originalSource;
        this.width = width;
    }


    public String getOriginalsource() {
        return originalSource;
    }

    public void setOriginalsource(String originalSource) {
        this.originalSource = originalSource;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }


}