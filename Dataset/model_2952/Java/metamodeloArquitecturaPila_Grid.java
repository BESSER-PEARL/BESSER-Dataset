





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_Grid extends ComplexComponent {

    private String rows;
    private String cols;



    public metamodeloArquitecturaPila_Grid(
        String rows,        String cols    ) {
        super(
        );
        this.rows = rows;
        this.cols = cols;
    }


    public String getRows() {
        return rows;
    }

    public void setRows(String rows) {
        this.rows = rows;
    }
    public String getCols() {
        return cols;
    }

    public void setCols(String cols) {
        this.cols = cols;
    }


}