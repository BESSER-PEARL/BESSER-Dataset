





import java.util.List;
import java.util.ArrayList;

public class xDstmdata_cExtchannel  {

    private String tID;
    private String tString;
    private String name;





    private xDstmdata_tTypes xdstmdata_ttypes;


    public xDstmdata_cExtchannel(
        String tID,        String tString,        String name    ) {
        this.tID = tID;
        this.tString = tString;
        this.name = name;
    }


    public String getTid() {
        return tID;
    }

    public void setTid(String tID) {
        this.tID = tID;
    }
    public String getTstring() {
        return tString;
    }

    public void setTstring(String tString) {
        this.tString = tString;
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