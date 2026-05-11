





import java.util.List;
import java.util.ArrayList;

public class workflow_DefaultDocument extends Document {

    private boolean placeholder;



    public workflow_DefaultDocument(
        boolean placeholder    ) {
        super(
        );
        this.placeholder = placeholder;
    }


    public boolean getPlaceholder() {
        return placeholder;
    }

    public void setPlaceholder(boolean placeholder) {
        this.placeholder = placeholder;
    }


}