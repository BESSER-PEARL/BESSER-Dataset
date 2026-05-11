





import java.util.List;
import java.util.ArrayList;

public class afpText_ICP extends structuredField {

    private String YCSize;
    private String YFilSize;
    private String XCOset;
    private String XCSize;
    private String XFilSize;
    private String YCOset;



    public afpText_ICP(
        String YCSize,        String YFilSize,        String XCOset,        String XCSize,        String XFilSize,        String YCOset    ) {
        super(
        );
        this.YCSize = YCSize;
        this.YFilSize = YFilSize;
        this.XCOset = XCOset;
        this.XCSize = XCSize;
        this.XFilSize = XFilSize;
        this.YCOset = YCOset;
    }


    public String getYcsize() {
        return YCSize;
    }

    public void setYcsize(String YCSize) {
        this.YCSize = YCSize;
    }
    public String getYfilsize() {
        return YFilSize;
    }

    public void setYfilsize(String YFilSize) {
        this.YFilSize = YFilSize;
    }
    public String getXcoset() {
        return XCOset;
    }

    public void setXcoset(String XCOset) {
        this.XCOset = XCOset;
    }
    public String getXcsize() {
        return XCSize;
    }

    public void setXcsize(String XCSize) {
        this.XCSize = XCSize;
    }
    public String getXfilsize() {
        return XFilSize;
    }

    public void setXfilsize(String XFilSize) {
        this.XFilSize = XFilSize;
    }
    public String getYcoset() {
        return YCOset;
    }

    public void setYcoset(String YCOset) {
        this.YCOset = YCOset;
    }


}