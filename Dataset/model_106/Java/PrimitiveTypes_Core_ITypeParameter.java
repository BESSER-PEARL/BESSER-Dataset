





import java.util.List;
import java.util.ArrayList;

public class PrimitiveTypes_Core_ITypeParameter extends Core_IJavaElement, Core_ISourceReference {

    private String bounds;



    public PrimitiveTypes_Core_ITypeParameter(
        String bounds    ) {
        super(
            String,            elementName,            String,            source        );
        this.bounds = bounds;
    }


    public String getBounds() {
        return bounds;
    }

    public void setBounds(String bounds) {
        this.bounds = bounds;
    }


}