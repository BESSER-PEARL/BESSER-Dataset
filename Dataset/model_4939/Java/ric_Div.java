





import java.util.List;
import java.util.ArrayList;

public class ric_Div extends IdentifiableComponent, ClassifiableComponent, EventComponent, BlockLevelComponent {

    private String align;



    public ric_Div(
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