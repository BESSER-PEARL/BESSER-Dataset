





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_DeclareCursorStatement extends BindingStatement {

    private boolean hold;
    private String forQuery;
    private String cursorType;
    private String cursorName;
    private String forStatementName;



    public syntax_dbl_DeclareCursorStatement(
        boolean hold,        String forQuery,        String cursorType,        String cursorName,        String forStatementName    ) {
        super(
        );
        this.hold = hold;
        this.forQuery = forQuery;
        this.cursorType = cursorType;
        this.cursorName = cursorName;
        this.forStatementName = forStatementName;
    }


    public boolean getHold() {
        return hold;
    }

    public void setHold(boolean hold) {
        this.hold = hold;
    }
    public String getForquery() {
        return forQuery;
    }

    public void setForquery(String forQuery) {
        this.forQuery = forQuery;
    }
    public String getCursortype() {
        return cursorType;
    }

    public void setCursortype(String cursorType) {
        this.cursorType = cursorType;
    }
    public String getCursorname() {
        return cursorName;
    }

    public void setCursorname(String cursorName) {
        this.cursorName = cursorName;
    }
    public String getForstatementname() {
        return forStatementName;
    }

    public void setForstatementname(String forStatementName) {
        this.forStatementName = forStatementName;
    }


}