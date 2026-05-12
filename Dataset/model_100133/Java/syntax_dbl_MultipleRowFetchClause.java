





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_MultipleRowFetchClause  {

    private String into;
    private boolean usingDescriptor;
    private String descriptor;
    private String rowsNumber;



    public syntax_dbl_MultipleRowFetchClause(
        String into,        boolean usingDescriptor,        String descriptor,        String rowsNumber    ) {
        this.into = into;
        this.usingDescriptor = usingDescriptor;
        this.descriptor = descriptor;
        this.rowsNumber = rowsNumber;
    }


    public String getInto() {
        return into;
    }

    public void setInto(String into) {
        this.into = into;
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