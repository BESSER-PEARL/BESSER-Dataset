





import java.util.List;
import java.util.ArrayList;

public class presentation_Table extends Composite {

    private String columnOrder;
    private String group3;
    private String headerVisible;
    private String topIndex;
    private String linesVisible;
    private String sortDirection;
    private String itemCount;
    private String selectionIndices;



    public presentation_Table(
        String columnOrder,        String group3,        String headerVisible,        String topIndex,        String linesVisible,        String sortDirection,        String itemCount,        String selectionIndices    ) {
        super(
        );
        this.columnOrder = columnOrder;
        this.group3 = group3;
        this.headerVisible = headerVisible;
        this.topIndex = topIndex;
        this.linesVisible = linesVisible;
        this.sortDirection = sortDirection;
        this.itemCount = itemCount;
        this.selectionIndices = selectionIndices;
    }


    public String getColumnorder() {
        return columnOrder;
    }

    public void setColumnorder(String columnOrder) {
        this.columnOrder = columnOrder;
    }
    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }
    public String getHeadervisible() {
        return headerVisible;
    }

    public void setHeadervisible(String headerVisible) {
        this.headerVisible = headerVisible;
    }
    public String getTopindex() {
        return topIndex;
    }

    public void setTopindex(String topIndex) {
        this.topIndex = topIndex;
    }
    public String getLinesvisible() {
        return linesVisible;
    }

    public void setLinesvisible(String linesVisible) {
        this.linesVisible = linesVisible;
    }
    public String getSortdirection() {
        return sortDirection;
    }

    public void setSortdirection(String sortDirection) {
        this.sortDirection = sortDirection;
    }
    public String getItemcount() {
        return itemCount;
    }

    public void setItemcount(String itemCount) {
        this.itemCount = itemCount;
    }
    public String getSelectionindices() {
        return selectionIndices;
    }

    public void setSelectionindices(String selectionIndices) {
        this.selectionIndices = selectionIndices;
    }


}