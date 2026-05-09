





import java.util.List;
import java.util.ArrayList;

public class presentation_TreeItem extends Item {

    private String checked;
    private String handle;
    private String group;
    private String grayed;
    private String expanded;
    private String texts;
    private String itemCount;





    private presentation_TreeItem presentation_treeitem;




    private presentation_Tree presentation_tree;




    private List<presentation_TreeItem> presentation_treeitems;




    private List<presentation_Tree> presentation_trees;




    private presentation_Tree presentation_tree;




    private presentation_Tree presentation_tree;




    private presentation_Tree presentation_tree;


    public presentation_TreeItem(
        String checked,        String handle,        String group,        String grayed,        String expanded,        String texts,        String itemCount    ) {
        super(
        );
        this.checked = checked;
        this.handle = handle;
        this.group = group;
        this.grayed = grayed;
        this.expanded = expanded;
        this.texts = texts;
        this.itemCount = itemCount;
        this.presentation_treeitems = new ArrayList<>();
        this.presentation_trees = new ArrayList<>();
    }

    public presentation_TreeItem(
        String checked,        String handle,        String group,        String grayed,        String expanded,        String texts,        String itemCount        ArrayList<presentation_TreeItem> presentation_treeitems,        ArrayList<presentation_Tree> presentation_trees    ) {
        this.checked = checked;
        this.handle = handle;
        this.group = group;
        this.grayed = grayed;
        this.expanded = expanded;
        this.texts = texts;
        this.itemCount = itemCount;
        this.presentation_treeitems = presentation_treeitems;
        this.presentation_trees = presentation_trees;
    }

    public String getChecked() {
        return checked;
    }

    public void setChecked(String checked) {
        this.checked = checked;
    }
    public String getHandle() {
        return handle;
    }

    public void setHandle(String handle) {
        this.handle = handle;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getGrayed() {
        return grayed;
    }

    public void setGrayed(String grayed) {
        this.grayed = grayed;
    }
    public String getExpanded() {
        return expanded;
    }

    public void setExpanded(String expanded) {
        this.expanded = expanded;
    }
    public String getTexts() {
        return texts;
    }

    public void setTexts(String texts) {
        this.texts = texts;
    }
    public String getItemcount() {
        return itemCount;
    }

    public void setItemcount(String itemCount) {
        this.itemCount = itemCount;
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
    public List<presentation_TreeItem> getPresentation_treeitems() {
        return presentation_treeitems;
    }

    public void addPresentation_treeitem(Presentation_treeitem presentation_treeitem) {
        this.presentation_treeitems.add(presentation_treeitem);
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

}