





import java.util.List;
import java.util.ArrayList;

public class ric_TextArea extends FormControl {

    private int cols;
    private boolean readonly;
    private int rols;



    public ric_TextArea(
        int cols,        boolean readonly,        int rols    ) {
        super(
        );
        this.cols = cols;
        this.readonly = readonly;
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
    public int getRols() {
        return rols;
    }

    public void setRols(int rols) {
        this.rols = rols;
    }


}