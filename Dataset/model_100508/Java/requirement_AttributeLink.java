





import java.util.List;
import java.util.ArrayList;

public class requirement_AttributeLink extends ObjectAttribute {

    private String partial;



    public requirement_AttributeLink(
        String partial    ) {
        super(
        );
        this.partial = partial;
    }


    public String getPartial() {
        return partial;
    }

    public void setPartial(String partial) {
        this.partial = partial;
    }


}