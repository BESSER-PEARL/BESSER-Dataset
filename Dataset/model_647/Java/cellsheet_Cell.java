





import java.util.List;
import java.util.ArrayList;

public class cellsheet_Cell extends HasId, HasA1 {

    private int colIndex;



    public cellsheet_Cell(
        int colIndex    ) {
        super(
        );
        this.colIndex = colIndex;
    }


    public int getColindex() {
        return colIndex;
    }

    public void setColindex(int colIndex) {
        this.colIndex = colIndex;
    }


}