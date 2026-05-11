





import java.util.List;
import java.util.ArrayList;

public class article_TreeFormatter extends Formatter {

    private int expandTo;
    private String expanded;
    private String selected;
    private String file;



    public article_TreeFormatter(
        int expandTo,        String expanded,        String selected,        String file    ) {
        super(
        );
        this.expandTo = expandTo;
        this.expanded = expanded;
        this.selected = selected;
        this.file = file;
    }


    public int getExpandto() {
        return expandTo;
    }

    public void setExpandto(int expandTo) {
        this.expandTo = expandTo;
    }
    public String getExpanded() {
        return expanded;
    }

    public void setExpanded(String expanded) {
        this.expanded = expanded;
    }
    public String getSelected() {
        return selected;
    }

    public void setSelected(String selected) {
        this.selected = selected;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }


}