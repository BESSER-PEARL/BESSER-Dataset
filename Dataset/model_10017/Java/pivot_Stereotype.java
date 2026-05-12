





import java.util.List;
import java.util.ArrayList;

public class pivot_Stereotype extends Class {






    private pivot_StereotypeExtender pivot_stereotypeextender;




    private List<pivot_StereotypeExtender> pivot_stereotypeextenders;




    private pivot_ElementExtension pivot_elementextension;


    public pivot_Stereotype(
    ) {
        super(
        );
        this.pivot_stereotypeextenders = new ArrayList<>();
    }

    public pivot_Stereotype(
        ArrayList<pivot_StereotypeExtender> pivot_stereotypeextenders    ) {
        this.pivot_stereotypeextenders = pivot_stereotypeextenders;
    }


    public pivot_StereotypeExtender getPivot_stereotypeextender() {
        return pivot_stereotypeextender;
    }

    public void setPivot_stereotypeextender(pivot_StereotypeExtender pivot_stereotypeextender) {
        this.pivot_stereotypeextender = pivot_stereotypeextender;
    }
    public List<pivot_StereotypeExtender> getPivot_stereotypeextenders() {
        return pivot_stereotypeextenders;
    }

    public void addPivot_stereotypeextender(Pivot_stereotypeextender pivot_stereotypeextender) {
        this.pivot_stereotypeextenders.add(pivot_stereotypeextender);
    }
    public pivot_ElementExtension getPivot_elementextension() {
        return pivot_elementextension;
    }

    public void setPivot_elementextension(pivot_ElementExtension pivot_elementextension) {
        this.pivot_elementextension = pivot_elementextension;
    }

}