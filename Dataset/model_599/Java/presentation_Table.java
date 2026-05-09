





import java.util.List;
import java.util.ArrayList;

public class presentation_Table extends Composite {

    private String selectionIndices;
    private String topIndex;
    private String columnOrder;
    private String linesVisible;
    private String headerVisible;
    private String group3;
    private String itemCount;
    private String sortDirection;



    public presentation_Table(
        String selectionIndices,        String topIndex,        String columnOrder,        String linesVisible,        String headerVisible,        String group3,        String itemCount,        String sortDirection    ) {
        super(
        );
        this.selectionIndices = selectionIndices;
        this.topIndex = topIndex;
        this.columnOrder = columnOrder;
        this.linesVisible = linesVisible;
        this.headerVisible = headerVisible;
        this.group3 = group3;
        this.itemCount = itemCount;
        this.sortDirection = sortDirection;
    }


    public String getSelectionindices() {
        return selectionIndices;
    }

    public void setSelectionindices(String selectionIndices) {
        this.selectionIndices = selectionIndices;
    }
    public String getTopindex() {
        return topIndex;
    }

    public void setTopindex(String topIndex) {
        this.topIndex = topIndex;
    }
    public String getColumnorder() {
        return columnOrder;
    }

    public void setColumnorder(String columnOrder) {
        this.columnOrder = columnOrder;
    }
    public String getLinesvisible() {
        return linesVisible;
    }

    public void setLinesvisible(String linesVisible) {
        this.linesVisible = linesVisible;
    }
    public String getHeadervisible() {
        return headerVisible;
    }

    public void setHeadervisible(String headerVisible) {
        this.headerVisible = headerVisible;
    }
    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }
    public String getItemcount() {
        return itemCount;
    }

    public void setItemcount(String itemCount) {
        this.itemCount = itemCount;
    }
    public String getSortdirection() {
        return sortDirection;
    }

    public void setSortdirection(String sortDirection) {
        this.sortDirection = sortDirection;
    }


}