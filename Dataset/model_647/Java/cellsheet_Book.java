





import java.util.List;
import java.util.ArrayList;

public class cellsheet_Book extends HasId, HasA1 {

    private String bookname;





    private cellsheet_Workspace cellsheet_workspace;




    private cellsheet_Workspace cellsheet_workspace;


    public cellsheet_Book(
        String bookname    ) {
        super(
        );
        this.bookname = bookname;
    }


    public String getBookname() {
        return bookname;
    }

    public void setBookname(String bookname) {
        this.bookname = bookname;
    }

    public cellsheet_Workspace getCellsheet_workspace() {
        return cellsheet_workspace;
    }

    public void setCellsheet_workspace(cellsheet_Workspace cellsheet_workspace) {
        this.cellsheet_workspace = cellsheet_workspace;
    }
    public cellsheet_Workspace getCellsheet_workspace() {
        return cellsheet_workspace;
    }

    public void setCellsheet_workspace(cellsheet_Workspace cellsheet_workspace) {
        this.cellsheet_workspace = cellsheet_workspace;
    }

}