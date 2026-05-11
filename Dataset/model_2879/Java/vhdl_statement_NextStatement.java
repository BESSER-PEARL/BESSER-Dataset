





import java.util.List;
import java.util.ArrayList;

public class vhdl_statement_NextStatement extends Statement {

    private String next;



    public vhdl_statement_NextStatement(
        String next    ) {
        super(
        );
        this.next = next;
    }


    public String getNext() {
        return next;
    }

    public void setNext(String next) {
        this.next = next;
    }


}