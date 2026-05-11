





import java.util.List;
import java.util.ArrayList;

public class ric_TextArea extends FormControl {

    private boolean readonly;
    private int cols;
    private int rols;



    public ric_TextArea(
        boolean readonly,        int cols,        int rols    ) {
        super(
        );
        this.readonly = readonly;
        this.cols = cols;
        this.rols = rols;
    }


    public boolean getReadonly() {
        return readonly;
    }

    public void setReadonly(boolean readonly) {
        this.readonly = readonly;
    }
    public int getCols() {
        return cols;
    }

    public void setCols(int cols) {
        this.cols = cols;
    }
    public int getRols() {
        return rols;
    }

    public void setRols(int rols) {
        this.rols = rols;
    }


}