





import java.util.List;
import java.util.ArrayList;

public class afpText_IOC extends structuredField {

    private String YMap;
    private String XoaOrent;
    private String XMap;
    private String ConData1;
    private String YoaOrent;
    private String ConData2;
    private String YoaOset;
    private String XoaOset;



    public afpText_IOC(
        String YMap,        String XoaOrent,        String XMap,        String ConData1,        String YoaOrent,        String ConData2,        String YoaOset,        String XoaOset    ) {
        super(
        );
        this.YMap = YMap;
        this.XoaOrent = XoaOrent;
        this.XMap = XMap;
        this.ConData1 = ConData1;
        this.YoaOrent = YoaOrent;
        this.ConData2 = ConData2;
        this.YoaOset = YoaOset;
        this.XoaOset = XoaOset;
    }


    public String getYmap() {
        return YMap;
    }

    public void setYmap(String YMap) {
        this.YMap = YMap;
    }
    public String getXoaorent() {
        return XoaOrent;
    }

    public void setXoaorent(String XoaOrent) {
        this.XoaOrent = XoaOrent;
    }
    public String getXmap() {
        return XMap;
    }

    public void setXmap(String XMap) {
        this.XMap = XMap;
    }
    public String getCondata1() {
        return ConData1;
    }

    public void setCondata1(String ConData1) {
        this.ConData1 = ConData1;
    }
    public String getYoaorent() {
        return YoaOrent;
    }

    public void setYoaorent(String YoaOrent) {
        this.YoaOrent = YoaOrent;
    }
    public String getCondata2() {
        return ConData2;
    }

    public void setCondata2(String ConData2) {
        this.ConData2 = ConData2;
    }
    public String getYoaoset() {
        return YoaOset;
    }

    public void setYoaoset(String YoaOset) {
        this.YoaOset = YoaOset;
    }
    public String getXoaoset() {
        return XoaOset;
    }

    public void setXoaoset(String XoaOset) {
        this.XoaOset = XoaOset;
    }


}