





import java.util.List;
import java.util.ArrayList;

public class ric_Paragraph extends IdentifiableComponent, ClassifiableComponent, InlineComponent, EventComponent {

    private String align;



    public ric_Paragraph(
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