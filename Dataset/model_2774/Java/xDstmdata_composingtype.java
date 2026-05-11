





import java.util.List;
import java.util.ArrayList;

public class xDstmdata_composingtype  {

    private String tString;
    private String tID;





    private xDstmdata_tMultitype xdstmdata_tmultitype;




    private xDstmdata_channel_specifier xdstmdata_channel_specifier;


    public xDstmdata_composingtype(
        String tString,        String tID    ) {
        this.tString = tString;
        this.tID = tID;
    }


    public String getTstring() {
        return tString;
    }

    public void setTstring(String tString) {
        this.tString = tString;
    }
    public String getTid() {
        return tID;
    }

    public void setTid(String tID) {
        this.tID = tID;
    }

    public xDstmdata_tMultitype getXdstmdata_tmultitype() {
        return xdstmdata_tmultitype;
    }

    public void setXdstmdata_tmultitype(xDstmdata_tMultitype xdstmdata_tmultitype) {
        this.xdstmdata_tmultitype = xdstmdata_tmultitype;
    }
    public xDstmdata_channel_specifier getXdstmdata_channel_specifier() {
        return xdstmdata_channel_specifier;
    }

    public void setXdstmdata_channel_specifier(xDstmdata_channel_specifier xdstmdata_channel_specifier) {
        this.xdstmdata_channel_specifier = xdstmdata_channel_specifier;
    }

}