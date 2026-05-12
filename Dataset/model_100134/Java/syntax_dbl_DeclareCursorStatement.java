





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_DeclareCursorStatement extends BindingStatement {

    private String cursorType;
    private String cursorName;
    private boolean hold;
    private String forStatementName;
    private String forQuery;



    public syntax_dbl_DeclareCursorStatement(
        String cursorType,        String cursorName,        boolean hold,        String forStatementName,        String forQuery    ) {
        super(
        );
        this.cursorType = cursorType;
        this.cursorName = cursorName;
        this.hold = hold;
        this.forStatementName = forStatementName;
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
    public boolean getHold() {
        return hold;
    }

    public void setHold(boolean hold) {
        this.hold = hold;
    }
    public String getForstatementname() {
        return forStatementName;
    }

    public void setForstatementname(String forStatementName) {
        this.forStatementName = forStatementName;
    }
    public String getForquery() {
        return forQuery;
    }

    public void setForquery(String forQuery) {
        this.forQuery = forQuery;
    }


}