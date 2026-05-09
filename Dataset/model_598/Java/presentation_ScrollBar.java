





import java.util.List;
import java.util.ArrayList;

public class presentation_ScrollBar extends Widget {

    private String increment;
    private String group;
    private String selection;
    private String size;
    private String pageIncrement;
    private String maximum;
    private String enabled;
    private String thumb;
    private String visible;
    private String minimum;





    private presentation_Scrollable presentation_scrollable;




    private presentation_Scrollable presentation_scrollable;




    private List<presentation_Scrollable> presentation_scrollables;


    public presentation_ScrollBar(
        String increment,        String group,        String selection,        String size,        String pageIncrement,        String maximum,        String enabled,        String thumb,        String visible,        String minimum    ) {
        super(
        );
        this.increment = increment;
        this.group = group;
        this.selection = selection;
        this.size = size;
        this.pageIncrement = pageIncrement;
        this.maximum = maximum;
        this.enabled = enabled;
        this.thumb = thumb;
        this.visible = visible;
        this.minimum = minimum;
        this.presentation_scrollables = new ArrayList<>();
    }

    public presentation_ScrollBar(
        String increment,        String group,        String selection,        String size,        String pageIncrement,        String maximum,        String enabled,        String thumb,        String visible,        String minimum        ArrayList<presentation_Scrollable> presentation_scrollables    ) {
        this.increment = increment;
        this.group = group;
        this.selection = selection;
        this.size = size;
        this.pageIncrement = pageIncrement;
        this.maximum = maximum;
        this.enabled = enabled;
        this.thumb = thumb;
        this.visible = visible;
        this.minimum = minimum;
        this.presentation_scrollables = presentation_scrollables;
    }

    public String getIncrement() {
        return increment;
    }

    public void setIncrement(String increment) {
        this.increment = increment;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getPageincrement() {
        return pageIncrement;
    }

    public void setPageincrement(String pageIncrement) {
        this.pageIncrement = pageIncrement;
    }
    public String getMaximum() {
        return maximum;
    }

    public void setMaximum(String maximum) {
        this.maximum = maximum;
    }
    public String getEnabled() {
        return enabled;
    }

    public void setEnabled(String enabled) {
        this.enabled = enabled;
    }
    public String getThumb() {
        return thumb;
    }

    public void setThumb(String thumb) {
        this.thumb = thumb;
    }
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }
    public String getMinimum() {
        return minimum;
    }

    public void setMinimum(String minimum) {
        this.minimum = minimum;
    }

    public presentation_Scrollable getPresentation_scrollable() {
        return presentation_scrollable;
    }

    public void setPresentation_scrollable(presentation_Scrollable presentation_scrollable) {
        this.presentation_scrollable = presentation_scrollable;
    }
    public presentation_Scrollable getPresentation_scrollable() {
        return presentation_scrollable;
    }

    public void setPresentation_scrollable(presentation_Scrollable presentation_scrollable) {
        this.presentation_scrollable = presentation_scrollable;
    }
    public List<presentation_Scrollable> getPresentation_scrollables() {
        return presentation_scrollables;
    }

    public void addPresentation_scrollable(Presentation_scrollable presentation_scrollable) {
        this.presentation_scrollables.add(presentation_scrollable);
    }

}