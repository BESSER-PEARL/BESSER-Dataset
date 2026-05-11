





import java.util.List;
import java.util.ArrayList;

public class ric_TextArea extends FormControl {

    private int rols;
    private int cols;
    private boolean readonly;



    public ric_TextArea(
        int rols,        int cols,        boolean readonly    ) {
        super(
        );
        this.rols = rols;
        this.cols = cols;
        this.readonly = readonly;
    }


    public int getRols() {
        return rols;
    }

    public void setRols(int rols) {
        this.rols = rols;
    }
    public int getCols() {
        return cols;
    }

    public void setCols(int cols) {
        this.cols = cols;
    }
    public boolean getReadonly() {
        return readonly;
    }

    public void setReadonly(boolean readonly) {
        this.readonly = readonly;
    }


}