





import java.util.List;
import java.util.ArrayList;

public class afpText_ObjectAreaSize extends triplet {

    private String XoaSize;
    private String YoaSize;
    private String SizeType;



    public afpText_ObjectAreaSize(
        String XoaSize,        String YoaSize,        String SizeType    ) {
        super(
        );
        this.XoaSize = XoaSize;
        this.YoaSize = YoaSize;
        this.SizeType = SizeType;
    }


    public String getXoasize() {
        return XoaSize;
    }

    public void setXoasize(String XoaSize) {
        this.XoaSize = XoaSize;
    }
    public String getYoasize() {
        return YoaSize;
    }

    public void setYoasize(String YoaSize) {
        this.YoaSize = YoaSize;
    }
    public String getSizetype() {
        return SizeType;
    }

    public void setSizetype(String SizeType) {
        this.SizeType = SizeType;
    }


}