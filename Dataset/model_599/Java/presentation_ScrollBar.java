





import java.util.List;
import java.util.ArrayList;

public class presentation_ScrollBar extends Widget {

    private String visible;
    private String minimum;
    private String enabled;
    private String size;
    private String maximum;
    private String selection;
    private String increment;
    private String thumb;
    private String pageIncrement;
    private String group;





    private presentation_Scrollable presentation_scrollable;




    private List<presentation_Scrollable> presentation_scrollables;




    private presentation_Scrollable presentation_scrollable;


    public presentation_ScrollBar(
        String visible,        String minimum,        String enabled,        String size,        String maximum,        String selection,        String increment,        String thumb,        String pageIncrement,        String group    ) {
        super(
        );
        this.visible = visible;
        this.minimum = minimum;
        this.enabled = enabled;
        this.size = size;
        this.maximum = maximum;
        this.selection = selection;
        this.increment = increment;
        this.thumb = thumb;
        this.pageIncrement = pageIncrement;
        this.group = group;
        this.presentation_scrollables = new ArrayList<>();
    }

    public presentation_ScrollBar(
        String visible,        String minimum,        String enabled,        String size,        String maximum,        String selection,        String increment,        String thumb,        String pageIncrement,        String group        ArrayList<presentation_Scrollable> presentation_scrollables    ) {
        this.visible = visible;
        this.minimum = minimum;
        this.enabled = enabled;
        this.size = size;
        this.maximum = maximum;
        this.selection = selection;
        this.increment = increment;
        this.thumb = thumb;
        this.pageIncrement = pageIncrement;
        this.group = group;
        this.presentation_scrollables = presentation_scrollables;
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
    public String getEnabled() {
        return enabled;
    }

    public void setEnabled(String enabled) {
        this.enabled = enabled;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getMaximum() {
        return maximum;
    }

    public void setMaximum(String maximum) {
        this.maximum = maximum;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }
    public String getIncrement() {
        return increment;
    }

    public void setIncrement(String increment) {
        this.increment = increment;
    }
    public String getThumb() {
        return thumb;
    }

    public void setThumb(String thumb) {
        this.thumb = thumb;
    }
    public String getPageincrement() {
        return pageIncrement;
    }

    public void setPageincrement(String pageIncrement) {
        this.pageIncrement = pageIncrement;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
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
    public presentation_Scrollable getPresentation_scrollable() {
        return presentation_scrollable;
    }

    public void setPresentation_scrollable(presentation_Scrollable presentation_scrollable) {
        this.presentation_scrollable = presentation_scrollable;
    }

}