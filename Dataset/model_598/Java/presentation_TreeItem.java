





import java.util.List;
import java.util.ArrayList;

public class presentation_TreeItem extends Item {

    private String texts;
    private String handle;
    private String expanded;
    private String checked;
    private String itemCount;
    private String grayed;
    private String group;





    private presentation_Tree presentation_tree;




    private presentation_Tree presentation_tree;




    private presentation_TreeItem presentation_treeitem;




    private presentation_TreeItem presentation_treeitem;




    private presentation_Tree presentation_tree;




    private List<presentation_Tree> presentation_trees;




    private presentation_Tree presentation_tree;


    public presentation_TreeItem(
        String texts,        String handle,        String expanded,        String checked,        String itemCount,        String grayed,        String group    ) {
        super(
        );
        this.texts = texts;
        this.handle = handle;
        this.expanded = expanded;
        this.checked = checked;
        this.itemCount = itemCount;
        this.grayed = grayed;
        this.group = group;
        this.presentation_trees = new ArrayList<>();
    }

    public presentation_TreeItem(
        String texts,        String handle,        String expanded,        String checked,        String itemCount,        String grayed,        String group        ArrayList<presentation_Tree> presentation_trees    ) {
        this.texts = texts;
        this.handle = handle;
        this.expanded = expanded;
        this.checked = checked;
        this.itemCount = itemCount;
        this.grayed = grayed;
        this.group = group;
        this.presentation_trees = presentation_trees;
    }

    public String getTexts() {
        return texts;
    }

    public void setTexts(String texts) {
        this.texts = texts;
    }
    public String getHandle() {
        return handle;
    }

    public void setHandle(String handle) {
        this.handle = handle;
    }
    public String getExpanded() {
        return expanded;
    }

    public void setExpanded(String expanded) {
        this.expanded = expanded;
    }
    public String getChecked() {
        return checked;
    }

    public void setChecked(String checked) {
        this.checked = checked;
    }
    public String getItemcount() {
        return itemCount;
    }

    public void setItemcount(String itemCount) {
        this.itemCount = itemCount;
    }
    public String getGrayed() {
        return grayed;
    }

    public void setGrayed(String grayed) {
        this.grayed = grayed;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
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
    public presentation_TreeItem getPresentation_treeitem() {
        return presentation_treeitem;
    }

    public void setPresentation_treeitem(presentation_TreeItem presentation_treeitem) {
        this.presentation_treeitem = presentation_treeitem;
    }
    public presentation_TreeItem getPresentation_treeitem() {
        return presentation_treeitem;
    }

    public void setPresentation_treeitem(presentation_TreeItem presentation_treeitem) {
        this.presentation_treeitem = presentation_treeitem;
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
    public presentation_Tree getPresentation_tree() {
        return presentation_tree;
    }

    public void setPresentation_tree(presentation_Tree presentation_tree) {
        this.presentation_tree = presentation_tree;
    }

}