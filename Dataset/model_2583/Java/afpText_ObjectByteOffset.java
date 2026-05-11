





import java.util.List;
import java.util.ArrayList;

public class afpText_ObjectByteOffset extends triplet {

    private String DirByHi;
    private String DirByOff;



    public afpText_ObjectByteOffset(
        String DirByHi,        String DirByOff    ) {
        super(
        );
        this.DirByHi = DirByHi;
        this.DirByOff = DirByOff;
    }


    public String getDirbyhi() {
        return DirByHi;
    }

    public void setDirbyhi(String DirByHi) {
        this.DirByHi = DirByHi;
    }
    public String getDirbyoff() {
        return DirByOff;
    }

    public void setDirbyoff(String DirByOff) {
        this.DirByOff = DirByOff;
    }


}