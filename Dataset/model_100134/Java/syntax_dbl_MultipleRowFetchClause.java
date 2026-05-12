





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_MultipleRowFetchClause  {

    private boolean usingDescriptor;
    private String descriptor;
    private String rowsNumber;



    public syntax_dbl_MultipleRowFetchClause(
        boolean usingDescriptor,        String descriptor,        String rowsNumber    ) {
        this.usingDescriptor = usingDescriptor;
        this.descriptor = descriptor;
        this.rowsNumber = rowsNumber;
    }


    public boolean getUsingdescriptor() {
        return usingDescriptor;
    }

    public void setUsingdescriptor(boolean usingDescriptor) {
        this.usingDescriptor = usingDescriptor;
    }
    public String getDescriptor() {
        return descriptor;
    }

    public void setDescriptor(String descriptor) {
        this.descriptor = descriptor;
    }
    public String getRowsnumber() {
        return rowsNumber;
    }

    public void setRowsnumber(String rowsNumber) {
        this.rowsNumber = rowsNumber;
    }


}