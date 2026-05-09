





import java.util.List;
import java.util.ArrayList;

public class cellsheet_AstEval  {

    private boolean isError;
    private String text;
    private String numberValue;





    private cellsheet_Ast cellsheet_ast;


    public cellsheet_AstEval(
        boolean isError,        String text,        String numberValue    ) {
        this.isError = isError;
        this.text = text;
        this.numberValue = numberValue;
    }


    public boolean getIserror() {
        return isError;
    }

    public void setIserror(boolean isError) {
        this.isError = isError;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getNumbervalue() {
        return numberValue;
    }

    public void setNumbervalue(String numberValue) {
        this.numberValue = numberValue;
    }

    public cellsheet_Ast getCellsheet_ast() {
        return cellsheet_ast;
    }

    public void setCellsheet_ast(cellsheet_Ast cellsheet_ast) {
        this.cellsheet_ast = cellsheet_ast;
    }

}