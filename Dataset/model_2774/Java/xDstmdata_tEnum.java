





import java.util.List;
import java.util.ArrayList;

public class xDstmdata_tEnum  {

    private String name;
    private String literals;





    private xDstmdata_tTypes xdstmdata_ttypes;


    public xDstmdata_tEnum(
        String name,        String literals    ) {
        this.name = name;
        this.literals = literals;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLiterals() {
        return literals;
    }

    public void setLiterals(String literals) {
        this.literals = literals;
    }

    public xDstmdata_tTypes getXdstmdata_ttypes() {
        return xdstmdata_ttypes;
    }

    public void setXdstmdata_ttypes(xDstmdata_tTypes xdstmdata_ttypes) {
        this.xdstmdata_ttypes = xdstmdata_ttypes;
    }

}