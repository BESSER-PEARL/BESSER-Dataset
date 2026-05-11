





import java.util.List;
import java.util.ArrayList;

public class document_Entry  {

    private boolean isItalic;
    private String text;
    private boolean isBold;





    private document_Table document_table;


    public document_Entry(
        boolean isItalic,        String text,        boolean isBold    ) {
        this.isItalic = isItalic;
        this.text = text;
        this.isBold = isBold;
    }


    public boolean getIsitalic() {
        return isItalic;
    }

    public void setIsitalic(boolean isItalic) {
        this.isItalic = isItalic;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public boolean getIsbold() {
        return isBold;
    }

    public void setIsbold(boolean isBold) {
        this.isBold = isBold;
    }

    public document_Table getDocument_table() {
        return document_table;
    }

    public void setDocument_table(document_Table document_table) {
        this.document_table = document_table;
    }

}