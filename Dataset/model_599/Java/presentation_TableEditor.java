





import java.util.List;
import java.util.ArrayList;

public class presentation_TableEditor extends ControlEditor {

    private String group1;
    private String dynamic;
    private String column;





    private List<presentation_TableItem> presentation_tableitems;


    public presentation_TableEditor(
        String group1,        String dynamic,        String column    ) {
        super(
        );
        this.group1 = group1;
        this.dynamic = dynamic;
        this.column = column;
        this.presentation_tableitems = new ArrayList<>();
    }

    public presentation_TableEditor(
        String group1,        String dynamic,        String column        ArrayList<presentation_TableItem> presentation_tableitems    ) {
        this.group1 = group1;
        this.dynamic = dynamic;
        this.column = column;
        this.presentation_tableitems = presentation_tableitems;
    }

    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }
    public String getDynamic() {
        return dynamic;
    }

    public void setDynamic(String dynamic) {
        this.dynamic = dynamic;
    }
    public String getColumn() {
        return column;
    }

    public void setColumn(String column) {
        this.column = column;
    }

    public List<presentation_TableItem> getPresentation_tableitems() {
        return presentation_tableitems;
    }

    public void addPresentation_tableitem(Presentation_tableitem presentation_tableitem) {
        this.presentation_tableitems.add(presentation_tableitem);
    }

}