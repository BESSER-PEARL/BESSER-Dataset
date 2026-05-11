





import java.util.List;
import java.util.ArrayList;

public class afpText_BDA extends structuredField {

    private String Flags;
    private String Xoffset;
    private String Yoffset;
    private String Data;



    public afpText_BDA(
        String Flags,        String Xoffset,        String Yoffset,        String Data    ) {
        super(
        );
        this.Flags = Flags;
        this.Xoffset = Xoffset;
        this.Yoffset = Yoffset;
        this.Data = Data;
    }


    public String getFlags() {
        return Flags;
    }

    public void setFlags(String Flags) {
        this.Flags = Flags;
    }
    public String getXoffset() {
        return Xoffset;
    }

    public void setXoffset(String Xoffset) {
        this.Xoffset = Xoffset;
    }
    public String getYoffset() {
        return Yoffset;
    }

    public void setYoffset(String Yoffset) {
        this.Yoffset = Yoffset;
    }
    public String getData() {
        return Data;
    }

    public void setData(String Data) {
        this.Data = Data;
    }


}