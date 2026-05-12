





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_FetchStatement extends BindingStatement {

    private String position;
    private String cursorName;
    private String into;
    private String relativePosition;



    public syntax_dbl_FetchStatement(
        String position,        String cursorName,        String into,        String relativePosition    ) {
        super(
        );
        this.position = position;
        this.cursorName = cursorName;
        this.into = into;
        this.relativePosition = relativePosition;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getCursorname() {
        return cursorName;
    }

    public void setCursorname(String cursorName) {
        this.cursorName = cursorName;
    }
    public String getInto() {
        return into;
    }

    public void setInto(String into) {
        this.into = into;
    }
    public String getRelativeposition() {
        return relativePosition;
    }

    public void setRelativeposition(String relativePosition) {
        this.relativePosition = relativePosition;
    }


}