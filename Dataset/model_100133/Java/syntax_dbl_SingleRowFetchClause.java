





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_SingleRowFetchClause  {

    private boolean usingDescriptor;
    private String into;



    public syntax_dbl_SingleRowFetchClause(
        boolean usingDescriptor,        String into    ) {
        this.usingDescriptor = usingDescriptor;
        this.into = into;
    }


    public boolean getUsingdescriptor() {
        return usingDescriptor;
    }

    public void setUsingdescriptor(boolean usingDescriptor) {
        this.usingDescriptor = usingDescriptor;
    }
    public String getInto() {
        return into;
    }

    public void setInto(String into) {
        this.into = into;
    }


}