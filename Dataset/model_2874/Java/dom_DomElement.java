





import java.util.List;
import java.util.ArrayList;

public class dom_DomElement  {

    private int column;
    private int line;





    private dom_DomElement dom_domelement;


    public dom_DomElement(
        int column,        int line    ) {
        this.column = column;
        this.line = line;
    }


    public int getColumn() {
        return column;
    }

    public void setColumn(int column) {
        this.column = column;
    }
    public int getLine() {
        return line;
    }

    public void setLine(int line) {
        this.line = line;
    }

    public dom_DomElement getDom_domelement() {
        return dom_domelement;
    }

    public void setDom_domelement(dom_DomElement dom_domelement) {
        this.dom_domelement = dom_domelement;
    }

}