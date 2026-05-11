





import java.util.List;
import java.util.ArrayList;

public class ric_Span extends IdentifiableComponent, InlineComponent, EventComponent, ClassifiableComponent {

    private String align;



    public ric_Span(
        String align    ) {
        super(
        );
        this.align = align;
    }


    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }


}