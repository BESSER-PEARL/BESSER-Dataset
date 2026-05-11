





import java.util.List;
import java.util.ArrayList;

public class swt_Tree extends Control {

    private String sortDirection;
    private boolean headerVisible;
    private boolean linesVisible;





    private swt_TreeColumn swt_treecolumn;




    private List<swt_TreeColumn> swt_treecolumns;


    public swt_Tree(
        String sortDirection,        boolean headerVisible,        boolean linesVisible    ) {
        super(
        );
        this.sortDirection = sortDirection;
        this.headerVisible = headerVisible;
        this.linesVisible = linesVisible;
        this.swt_treecolumns = new ArrayList<>();
    }

    public swt_Tree(
        String sortDirection,        boolean headerVisible,        boolean linesVisible        ArrayList<swt_TreeColumn> swt_treecolumns    ) {
        this.sortDirection = sortDirection;
        this.headerVisible = headerVisible;
        this.linesVisible = linesVisible;
        this.swt_treecolumns = swt_treecolumns;
    }

    public String getSortdirection() {
        return sortDirection;
    }

    public void setSortdirection(String sortDirection) {
        this.sortDirection = sortDirection;
    }
    public boolean getHeadervisible() {
        return headerVisible;
    }

    public void setHeadervisible(boolean headerVisible) {
        this.headerVisible = headerVisible;
    }
    public boolean getLinesvisible() {
        return linesVisible;
    }

    public void setLinesvisible(boolean linesVisible) {
        this.linesVisible = linesVisible;
    }

    public swt_TreeColumn getSwt_treecolumn() {
        return swt_treecolumn;
    }

    public void setSwt_treecolumn(swt_TreeColumn swt_treecolumn) {
        this.swt_treecolumn = swt_treecolumn;
    }
    public List<swt_TreeColumn> getSwt_treecolumns() {
        return swt_treecolumns;
    }

    public void addSwt_treecolumn(Swt_treecolumn swt_treecolumn) {
        this.swt_treecolumns.add(swt_treecolumn);
    }

}