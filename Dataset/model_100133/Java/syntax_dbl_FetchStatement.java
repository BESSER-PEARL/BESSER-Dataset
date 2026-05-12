





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_FetchStatement extends BindingStatement {

    private String cursorName;
    private String position;
    private String relativePosition;



    public syntax_dbl_FetchStatement(
        String cursorName,        String position,        String relativePosition    ) {
        super(
        );
        this.cursorName = cursorName;
        this.position = position;
        this.relativePosition = relativePosition;
    }


    public String getCursorname() {
        return cursorName;
    }

    public void setCursorname(String cursorName) {
        this.cursorName = cursorName;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getRelativeposition() {
        return relativePosition;
    }

    public void setRelativeposition(String relativePosition) {
        this.relativePosition = relativePosition;
    }


}