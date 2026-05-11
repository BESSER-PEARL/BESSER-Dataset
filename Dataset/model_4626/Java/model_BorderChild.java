





import java.util.List;
import java.util.ArrayList;

public class model_BorderChild extends Child {

    private String alignment;





    private model_BorderContainer model_bordercontainer;


    public model_BorderChild(
        String alignment    ) {
        super(
        );
        this.alignment = alignment;
    }


    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
        this.alignment = alignment;
    }

    public model_BorderContainer getModel_bordercontainer() {
        return model_bordercontainer;
    }

    public void setModel_bordercontainer(model_BorderContainer model_bordercontainer) {
        this.model_bordercontainer = model_bordercontainer;
    }

}