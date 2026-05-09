





import java.util.List;
import java.util.ArrayList;

public class presentation_TableColumn extends Item {

    private String resizable;
    private String alignment;
    private String group;
    private String toolTipText;
    private String moveable;
    private String width;





    private presentation_Table presentation_table;




    private presentation_Table presentation_table;




    private List<presentation_Table> presentation_tables;


    public presentation_TableColumn(
        String resizable,        String alignment,        String group,        String toolTipText,        String moveable,        String width    ) {
        super(
        );
        this.resizable = resizable;
        this.alignment = alignment;
        this.group = group;
        this.toolTipText = toolTipText;
        this.moveable = moveable;
        this.width = width;
        this.presentation_tables = new ArrayList<>();
    }

    public presentation_TableColumn(
        String resizable,        String alignment,        String group,        String toolTipText,        String moveable,        String width        ArrayList<presentation_Table> presentation_tables    ) {
        this.resizable = resizable;
        this.alignment = alignment;
        this.group = group;
        this.toolTipText = toolTipText;
        this.moveable = moveable;
        this.width = width;
        this.presentation_tables = presentation_tables;
    }

    public String getResizable() {
        return resizable;
    }

    public void setResizable(String resizable) {
        this.resizable = resizable;
    }
    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
        this.alignment = alignment;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getTooltiptext() {
        return toolTipText;
    }

    public void setTooltiptext(String toolTipText) {
        this.toolTipText = toolTipText;
    }
    public String getMoveable() {
        return moveable;
    }

    public void setMoveable(String moveable) {
        this.moveable = moveable;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }

    public presentation_Table getPresentation_table() {
        return presentation_table;
    }

    public void setPresentation_table(presentation_Table presentation_table) {
        this.presentation_table = presentation_table;
    }
    public presentation_Table getPresentation_table() {
        return presentation_table;
    }

    public void setPresentation_table(presentation_Table presentation_table) {
        this.presentation_table = presentation_table;
    }
    public List<presentation_Table> getPresentation_tables() {
        return presentation_tables;
    }

    public void addPresentation_table(Presentation_table presentation_table) {
        this.presentation_tables.add(presentation_table);
    }

}