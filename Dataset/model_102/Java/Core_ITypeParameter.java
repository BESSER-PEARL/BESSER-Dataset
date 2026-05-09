





import java.util.List;
import java.util.ArrayList;

public class Core_ITypeParameter extends ISourceReference, IJavaElement {

    private String bounds;



    public Core_ITypeParameter(
        String bounds    ) {
        super(
        );
        this.bounds = bounds;
    }


    public String getBounds() {
        return bounds;
    }

    public void setBounds(String bounds) {
        this.bounds = bounds;
    }


}