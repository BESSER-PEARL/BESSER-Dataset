





import java.util.List;
import java.util.ArrayList;

public class window  {

    private int columns;
    private int lines;
    private int y;
    private int x;
    private None current;
    private String _main;



    public window(
        int columns,        int lines,        int y,        int x,        None current,        String _main    ) {
        this.columns = columns;
        this.lines = lines;
        this.y = y;
        this.x = x;
        this.current = current;
        this._main = _main;
    }


    public int getColumns() {
        return columns;
    }

    public void setColumns(int columns) {
        this.columns = columns;
    }
    public int getLines() {
        return lines;
    }

    public void setLines(int lines) {
        this.lines = lines;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public None getCurrent() {
        return current;
    }

    public void setCurrent(None current) {
        this.current = current;
    }
    public String get_main() {
        return _main;
    }

    public void set_main(String _main) {
        this._main = _main;
    }


}