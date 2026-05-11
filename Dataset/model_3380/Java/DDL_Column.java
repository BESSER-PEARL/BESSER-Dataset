





import java.util.List;
import java.util.ArrayList;

public class DDL_Column extends NamedElement {

    private boolean columnNull;



    public DDL_Column(
        boolean columnNull    ) {
        super(
        );
        this.columnNull = columnNull;
    }


    public boolean getColumnnull() {
        return columnNull;
    }

    public void setColumnnull(boolean columnNull) {
        this.columnNull = columnNull;
    }


}