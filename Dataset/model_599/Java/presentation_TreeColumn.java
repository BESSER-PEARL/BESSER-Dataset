





import java.util.List;
import java.util.ArrayList;

public class presentation_TreeColumn extends Item {

    private String alignment;
    private String resizable;
    private String width;
    private String moveable;
    private String group;
    private String toolTipText;





    private presentation_Tree presentation_tree;




    private presentation_Tree presentation_tree;




    private List<presentation_Tree> presentation_trees;


    public presentation_TreeColumn(
        String alignment,        String resizable,        String width,        String moveable,        String group,        String toolTipText    ) {
        super(
        );
        this.alignment = alignment;
        this.resizable = resizable;
        this.width = width;
        this.moveable = moveable;
        this.group = group;
        this.toolTipText = toolTipText;
        this.presentation_trees = new ArrayList<>();
    }

    public presentation_TreeColumn(
        String alignment,        String resizable,        String width,        String moveable,        String group,        String toolTipText        ArrayList<presentation_Tree> presentation_trees    ) {
        this.alignment = alignment;
        this.resizable = resizable;
        this.width = width;
        this.moveable = moveable;
        this.group = group;
        this.toolTipText = toolTipText;
        this.presentation_trees = presentation_trees;
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
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getMoveable() {
        return moveable;
    }

    public void setMoveable(String moveable) {
        this.moveable = moveable;
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

    public presentation_Tree getPresentation_tree() {
        return presentation_tree;
    }

    public void setPresentation_tree(presentation_Tree presentation_tree) {
        this.presentation_tree = presentation_tree;
    }
    public presentation_Tree getPresentation_tree() {
        return presentation_tree;
    }

    public void setPresentation_tree(presentation_Tree presentation_tree) {
        this.presentation_tree = presentation_tree;
    }
    public List<presentation_Tree> getPresentation_trees() {
        return presentation_trees;
    }

    public void addPresentation_tree(Presentation_tree presentation_tree) {
        this.presentation_trees.add(presentation_tree);
    }

}