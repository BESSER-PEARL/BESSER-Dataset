





import java.util.List;
import java.util.ArrayList;

public class ric_Div extends BlockLevelComponent, ClassifiableComponent, IdentifiableComponent, EventComponent {

    private String align;





    private List<ric_List> ric_lists;


    public ric_Div(
        String align    ) {
        super(
        );
        this.align = align;
        this.ric_lists = new ArrayList<>();
    }

    public ric_Div(
        String align        ArrayList<ric_List> ric_lists    ) {
        this.align = align;
        this.ric_lists = ric_lists;
    }

    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }

    public List<ric_List> getRic_lists() {
        return ric_lists;
    }

    public void addRic_list(Ric_list ric_list) {
        this.ric_lists.add(ric_list);
    }

}