





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelNote extends TextPosition, TextContent, DiagramModelObject {

    private int borderType;



    public model_DiagramModelNote(
        int borderType    ) {
        super(
        );
        this.borderType = borderType;
    }


    public int getBordertype() {
        return borderType;
    }

    public void setBordertype(int borderType) {
        this.borderType = borderType;
    }


}