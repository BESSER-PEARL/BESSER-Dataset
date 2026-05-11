





import java.util.List;
import java.util.ArrayList;

public class cobol_commons_LabellableElement extends Commentable {

    private String label;



    public cobol_commons_LabellableElement(
        String label    ) {
        super(
        );
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}