





import java.util.List;
import java.util.ArrayList;

public class webapp_Text extends Widget {

    private int columnNumber;



    public webapp_Text(
        int columnNumber    ) {
        super(
        );
        this.columnNumber = columnNumber;
    }


    public int getColumnnumber() {
        return columnNumber;
    }

    public void setColumnnumber(int columnNumber) {
        this.columnNumber = columnNumber;
    }


}