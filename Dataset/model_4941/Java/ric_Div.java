





import java.util.List;
import java.util.ArrayList;

public class ric_Div extends ClassifiableComponent, IdentifiableComponent, EventComponent, BlockLevelComponent {

    private String align;





    private List<ric_Fieldset> ric_fieldsets;


    public ric_Div(
        String align    ) {
        super(
        );
        this.align = align;
        this.ric_fieldsets = new ArrayList<>();
    }

    public ric_Div(
        String align        ArrayList<ric_Fieldset> ric_fieldsets    ) {
        this.align = align;
        this.ric_fieldsets = ric_fieldsets;
    }

    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }

    public List<ric_Fieldset> getRic_fieldsets() {
        return ric_fieldsets;
    }

    public void addRic_fieldset(Ric_fieldset ric_fieldset) {
        this.ric_fieldsets.add(ric_fieldset);
    }

}