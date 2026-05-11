





import java.util.List;
import java.util.ArrayList;

public class afpText_FontDescriptorSpecification extends triplet {

    private String FtWtClass;
    private String FtHeight;
    private String FtWdClass;
    private String FtWidth;
    private String FtUsFlags;
    private String FtDsFlags;



    public afpText_FontDescriptorSpecification(
        String FtWtClass,        String FtHeight,        String FtWdClass,        String FtWidth,        String FtUsFlags,        String FtDsFlags    ) {
        super(
        );
        this.FtWtClass = FtWtClass;
        this.FtHeight = FtHeight;
        this.FtWdClass = FtWdClass;
        this.FtWidth = FtWidth;
        this.FtUsFlags = FtUsFlags;
        this.FtDsFlags = FtDsFlags;
    }


    public String getFtwtclass() {
        return FtWtClass;
    }

    public void setFtwtclass(String FtWtClass) {
        this.FtWtClass = FtWtClass;
    }
    public String getFtheight() {
        return FtHeight;
    }

    public void setFtheight(String FtHeight) {
        this.FtHeight = FtHeight;
    }
    public String getFtwdclass() {
        return FtWdClass;
    }

    public void setFtwdclass(String FtWdClass) {
        this.FtWdClass = FtWdClass;
    }
    public String getFtwidth() {
        return FtWidth;
    }

    public void setFtwidth(String FtWidth) {
        this.FtWidth = FtWidth;
    }
    public String getFtusflags() {
        return FtUsFlags;
    }

    public void setFtusflags(String FtUsFlags) {
        this.FtUsFlags = FtUsFlags;
    }
    public String getFtdsflags() {
        return FtDsFlags;
    }

    public void setFtdsflags(String FtDsFlags) {
        this.FtDsFlags = FtDsFlags;
    }


}