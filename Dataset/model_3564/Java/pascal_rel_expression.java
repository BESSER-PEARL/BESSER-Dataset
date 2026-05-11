





import java.util.List;
import java.util.ArrayList;

public class pascal_rel_expression extends expression {

    private String op;
    private String open;
    private String first;
    private String close;
    private String second;



    public pascal_rel_expression(
        String op,        String open,        String first,        String close,        String second    ) {
        super(
        );
        this.op = op;
        this.open = open;
        this.first = first;
        this.close = close;
        this.second = second;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }
    public String getOpen() {
        return open;
    }

    public void setOpen(String open) {
        this.open = open;
    }
    public String getFirst() {
        return first;
    }

    public void setFirst(String first) {
        this.first = first;
    }
    public String getClose() {
        return close;
    }

    public void setClose(String close) {
        this.close = close;
    }
    public String getSecond() {
        return second;
    }

    public void setSecond(String second) {
        this.second = second;
    }


}