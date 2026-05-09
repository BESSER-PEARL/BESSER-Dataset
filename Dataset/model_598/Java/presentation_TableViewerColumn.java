





import java.util.List;
import java.util.ArrayList;

public class presentation_TableViewerColumn extends ViewerColumn {

    private String group;
    private String width;
    private String text;





    private List<presentation_TableColumn> presentation_tablecolumns;


    public presentation_TableViewerColumn(
        String group,        String width,        String text    ) {
        super(
        );
        this.group = group;
        this.width = width;
        this.text = text;
        this.presentation_tablecolumns = new ArrayList<>();
    }

    public presentation_TableViewerColumn(
        String group,        String width,        String text        ArrayList<presentation_TableColumn> presentation_tablecolumns    ) {
        this.group = group;
        this.width = width;
        this.text = text;
        this.presentation_tablecolumns = presentation_tablecolumns;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public List<presentation_TableColumn> getPresentation_tablecolumns() {
        return presentation_tablecolumns;
    }

    public void addPresentation_tablecolumn(Presentation_tablecolumn presentation_tablecolumn) {
        this.presentation_tablecolumns.add(presentation_tablecolumn);
    }

}