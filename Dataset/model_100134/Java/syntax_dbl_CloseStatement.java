





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_CloseStatement extends BindingStatement {

    private String cursor;



    public syntax_dbl_CloseStatement(
        String cursor    ) {
        super(
        );
        this.cursor = cursor;
    }


    public String getCursor() {
        return cursor;
    }

    public void setCursor(String cursor) {
        this.cursor = cursor;
    }


}