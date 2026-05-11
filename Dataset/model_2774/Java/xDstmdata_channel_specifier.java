





import java.util.List;
import java.util.ArrayList;

public class xDstmdata_channel_specifier  {

    private String type;





    private xDstmdata_vVariable xdstmdata_vvariable;




    private xDstmdata_cIntchannel xdstmdata_cintchannel;




    private xDstmdata_subtype xdstmdata_subtype;




    private xDstmdata_cExtchannel xdstmdata_cextchannel;


    public xDstmdata_channel_specifier(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public xDstmdata_vVariable getXdstmdata_vvariable() {
        return xdstmdata_vvariable;
    }

    public void setXdstmdata_vvariable(xDstmdata_vVariable xdstmdata_vvariable) {
        this.xdstmdata_vvariable = xdstmdata_vvariable;
    }
    public xDstmdata_cIntchannel getXdstmdata_cintchannel() {
        return xdstmdata_cintchannel;
    }

    public void setXdstmdata_cintchannel(xDstmdata_cIntchannel xdstmdata_cintchannel) {
        this.xdstmdata_cintchannel = xdstmdata_cintchannel;
    }
    public xDstmdata_subtype getXdstmdata_subtype() {
        return xdstmdata_subtype;
    }

    public void setXdstmdata_subtype(xDstmdata_subtype xdstmdata_subtype) {
        this.xdstmdata_subtype = xdstmdata_subtype;
    }
    public xDstmdata_cExtchannel getXdstmdata_cextchannel() {
        return xdstmdata_cextchannel;
    }

    public void setXdstmdata_cextchannel(xDstmdata_cExtchannel xdstmdata_cextchannel) {
        this.xdstmdata_cextchannel = xdstmdata_cextchannel;
    }

}