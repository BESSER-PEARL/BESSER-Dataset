





import java.util.List;
import java.util.ArrayList;

public class presentation_Tree extends Composite {

    private String headerVisible;
    private String sortDirection;
    private String linesVisible;
    private String group3;
    private String itemCount;
    private String columnOrder;



    public presentation_Tree(
        String headerVisible,        String sortDirection,        String linesVisible,        String group3,        String itemCount,        String columnOrder    ) {
        super(
        );
        this.headerVisible = headerVisible;
        this.sortDirection = sortDirection;
        this.linesVisible = linesVisible;
        this.group3 = group3;
        this.itemCount = itemCount;
        this.columnOrder = columnOrder;
    }


    public String getHeadervisible() {
        return headerVisible;
    }

    public void setHeadervisible(String headerVisible) {
        this.headerVisible = headerVisible;
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
    public String getColumnorder() {
        return columnOrder;
    }

    public void setColumnorder(String columnOrder) {
        this.columnOrder = columnOrder;
    }


}