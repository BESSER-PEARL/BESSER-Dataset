





import java.util.List;
import java.util.ArrayList;

public class xDstmdata_cIntchannel  {

    private int bound;
    private String name;
    private String tID;
    private String tString;





    private xDstmdata_tTypes xdstmdata_ttypes;


    public xDstmdata_cIntchannel(
        int bound,        String name,        String tID,        String tString    ) {
        this.bound = bound;
        this.name = name;
        this.tID = tID;
        this.tString = tString;
    }


    public int getBound() {
        return bound;
    }

    public void setBound(int bound) {
        this.bound = bound;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
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

    public xDstmdata_tTypes getXdstmdata_ttypes() {
        return xdstmdata_ttypes;
    }

    public void setXdstmdata_ttypes(xDstmdata_tTypes xdstmdata_ttypes) {
        this.xdstmdata_ttypes = xdstmdata_ttypes;
    }

}