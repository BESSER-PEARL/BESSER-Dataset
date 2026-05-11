





import java.util.List;
import java.util.ArrayList;

public class xDstmdata_tCompound  {

    private String name;





    private xDstmdata_tTypes xdstmdata_ttypes;


    public xDstmdata_tCompound(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public xDstmdata_tTypes getXdstmdata_ttypes() {
        return xdstmdata_ttypes;
    }

    public void setXdstmdata_ttypes(xDstmdata_tTypes xdstmdata_ttypes) {
        this.xdstmdata_ttypes = xdstmdata_ttypes;
    }

}