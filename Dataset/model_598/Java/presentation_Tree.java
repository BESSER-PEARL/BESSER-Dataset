





import java.util.List;
import java.util.ArrayList;

public class presentation_Tree extends Composite {

    private String itemCount;
    private String group3;
    private String sortDirection;
    private String linesVisible;
    private String columnOrder;
    private String headerVisible;



    public presentation_Tree(
        String itemCount,        String group3,        String sortDirection,        String linesVisible,        String columnOrder,        String headerVisible    ) {
        super(
        );
        this.itemCount = itemCount;
        this.group3 = group3;
        this.sortDirection = sortDirection;
        this.linesVisible = linesVisible;
        this.columnOrder = columnOrder;
        this.headerVisible = headerVisible;
    }


    public String getItemcount() {
        return itemCount;
    }

    public void setItemcount(String itemCount) {
        this.itemCount = itemCount;
    }
    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }
    public String getSortdirection() {
        return sortDirection;
    }

    public void setSortdirection(String sortDirection) {
        this.sortDirection = sortDirection;
    }
    public String getLinesvisible() {
        return linesVisible;
    }

    public void setLinesvisible(String linesVisible) {
        this.linesVisible = linesVisible;
    }
    public String getColumnorder() {
        return columnOrder;
    }

    public void setColumnorder(String columnOrder) {
        this.columnOrder = columnOrder;
    }
    public String getHeadervisible() {
        return headerVisible;
    }

    public void setHeadervisible(String headerVisible) {
        this.headerVisible = headerVisible;
    }


}