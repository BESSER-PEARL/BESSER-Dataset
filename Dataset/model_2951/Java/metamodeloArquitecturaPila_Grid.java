





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_Grid extends ComplexComponent {

    private String cols;
    private String rows;



    public metamodeloArquitecturaPila_Grid(
        String cols,        String rows    ) {
        super(
        );
        this.cols = cols;
        this.rows = rows;
    }


    public String getCols() {
        return cols;
    }

    public void setCols(String cols) {
        this.cols = cols;
    }
    public String getRows() {
        return rows;
    }

    public void setRows(String rows) {
        this.rows = rows;
    }


}