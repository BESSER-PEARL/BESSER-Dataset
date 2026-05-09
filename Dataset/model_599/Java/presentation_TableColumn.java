





import java.util.List;
import java.util.ArrayList;

public class presentation_TableColumn extends Item {

    private String width;
    private String alignment;
    private String resizable;
    private String moveable;
    private String toolTipText;
    private String group;





    private presentation_Table presentation_table;




    private List<presentation_Table> presentation_tables;




    private presentation_Table presentation_table;


    public presentation_TableColumn(
        String width,        String alignment,        String resizable,        String moveable,        String toolTipText,        String group    ) {
        super(
        );
        this.width = width;
        this.alignment = alignment;
        this.resizable = resizable;
        this.moveable = moveable;
        this.toolTipText = toolTipText;
        this.group = group;
        this.presentation_tables = new ArrayList<>();
    }

    public presentation_TableColumn(
        String width,        String alignment,        String resizable,        String moveable,        String toolTipText,        String group        ArrayList<presentation_Table> presentation_tables    ) {
        this.width = width;
        this.alignment = alignment;
        this.resizable = resizable;
        this.moveable = moveable;
        this.toolTipText = toolTipText;
        this.group = group;
        this.presentation_tables = presentation_tables;
    }

    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
        this.alignment = alignment;
    }
    public String getResizable() {
        return resizable;
    }

    public void setResizable(String resizable) {
        this.resizable = resizable;
    }
    public String getMoveable() {
        return moveable;
    }

    public void setMoveable(String moveable) {
        this.moveable = moveable;
    }
    public String getTooltiptext() {
        return toolTipText;
    }

    public void setTooltiptext(String toolTipText) {
        this.toolTipText = toolTipText;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
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
    public presentation_Table getPresentation_table() {
        return presentation_table;
    }

    public void setPresentation_table(presentation_Table presentation_table) {
        this.presentation_table = presentation_table;
    }

}