





import java.util.List;
import java.util.ArrayList;

public class swt_List extends AbstractList {

    private String multiplicityStyle;
    private String selection;
    private int selectionIndices;



    public swt_List(
        String multiplicityStyle,        String selection,        int selectionIndices    ) {
        super(
        );
        this.multiplicityStyle = multiplicityStyle;
        this.selection = selection;
        this.selectionIndices = selectionIndices;
    }


    public String getMultiplicitystyle() {
        return multiplicityStyle;
    }

    public void setMultiplicitystyle(String multiplicityStyle) {
        this.multiplicityStyle = multiplicityStyle;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }
    public int getSelectionindices() {
        return selectionIndices;
    }

    public void setSelectionindices(int selectionIndices) {
        this.selectionIndices = selectionIndices;
    }


}