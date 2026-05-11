





import java.util.List;
import java.util.ArrayList;

public class afpText_IID extends structuredField {

    private String YBase;
    private String ConData1;
    private String XSize;
    private String XCSizeD;
    private String ConData2;
    private String XUnits;
    private String XBase;
    private String YUnits;
    private String YCSizeD;
    private String YSize;
    private String ConData3;
    private String Color;



    public afpText_IID(
        String YBase,        String ConData1,        String XSize,        String XCSizeD,        String ConData2,        String XUnits,        String XBase,        String YUnits,        String YCSizeD,        String YSize,        String ConData3,        String Color    ) {
        super(
        );
        this.YBase = YBase;
        this.ConData1 = ConData1;
        this.XSize = XSize;
        this.XCSizeD = XCSizeD;
        this.ConData2 = ConData2;
        this.XUnits = XUnits;
        this.XBase = XBase;
        this.YUnits = YUnits;
        this.YCSizeD = YCSizeD;
        this.YSize = YSize;
        this.ConData3 = ConData3;
        this.Color = Color;
    }


    public String getYbase() {
        return YBase;
    }

    public void setYbase(String YBase) {
        this.YBase = YBase;
    }
    public String getCondata1() {
        return ConData1;
    }

    public void setCondata1(String ConData1) {
        this.ConData1 = ConData1;
    }
    public String getXsize() {
        return XSize;
    }

    public void setXsize(String XSize) {
        this.XSize = XSize;
    }
    public String getXcsized() {
        return XCSizeD;
    }

    public void setXcsized(String XCSizeD) {
        this.XCSizeD = XCSizeD;
    }
    public String getCondata2() {
        return ConData2;
    }

    public void setCondata2(String ConData2) {
        this.ConData2 = ConData2;
    }
    public String getXunits() {
        return XUnits;
    }

    public void setXunits(String XUnits) {
        this.XUnits = XUnits;
    }
    public String getXbase() {
        return XBase;
    }

    public void setXbase(String XBase) {
        this.XBase = XBase;
    }
    public String getYunits() {
        return YUnits;
    }

    public void setYunits(String YUnits) {
        this.YUnits = YUnits;
    }
    public String getYcsized() {
        return YCSizeD;
    }

    public void setYcsized(String YCSizeD) {
        this.YCSizeD = YCSizeD;
    }
    public String getYsize() {
        return YSize;
    }

    public void setYsize(String YSize) {
        this.YSize = YSize;
    }
    public String getCondata3() {
        return ConData3;
    }

    public void setCondata3(String ConData3) {
        this.ConData3 = ConData3;
    }
    public String getColor() {
        return Color;
    }

    public void setColor(String Color) {
        this.Color = Color;
    }


}