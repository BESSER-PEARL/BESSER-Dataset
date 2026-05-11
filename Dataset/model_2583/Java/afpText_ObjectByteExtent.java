





import java.util.List;
import java.util.ArrayList;

public class afpText_ObjectByteExtent extends triplet {

    private String ByteExt;
    private String ByteExtHi;



    public afpText_ObjectByteExtent(
        String ByteExt,        String ByteExtHi    ) {
        super(
        );
        this.ByteExt = ByteExt;
        this.ByteExtHi = ByteExtHi;
    }


    public String getByteext() {
        return ByteExt;
    }

    public void setByteext(String ByteExt) {
        this.ByteExt = ByteExt;
    }
    public String getByteexthi() {
        return ByteExtHi;
    }

    public void setByteexthi(String ByteExtHi) {
        this.ByteExtHi = ByteExtHi;
    }


}