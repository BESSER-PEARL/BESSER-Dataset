





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_ParamPrint  {

    private float vertPosData;
    private float fontHightData;
    private float horzPosLeftBorder;
    private float horzPosValues;
    private float vertLineSpace;
    private String dateStamp;
    private float fontHightHeader;
    private float vertPosHeader;





    private MachineLibrary_NodeSpecialConfiguration machinelibrary_nodespecialconfiguration;


    public MachineLibrary_ParamPrint(
        float vertPosData,        float fontHightData,        float horzPosLeftBorder,        float horzPosValues,        float vertLineSpace,        String dateStamp,        float fontHightHeader,        float vertPosHeader    ) {
        this.vertPosData = vertPosData;
        this.fontHightData = fontHightData;
        this.horzPosLeftBorder = horzPosLeftBorder;
        this.horzPosValues = horzPosValues;
        this.vertLineSpace = vertLineSpace;
        this.dateStamp = dateStamp;
        this.fontHightHeader = fontHightHeader;
        this.vertPosHeader = vertPosHeader;
    }


    public float getVertposdata() {
        return vertPosData;
    }

    public void setVertposdata(float vertPosData) {
        this.vertPosData = vertPosData;
    }
    public float getFonthightdata() {
        return fontHightData;
    }

    public void setFonthightdata(float fontHightData) {
        this.fontHightData = fontHightData;
    }
    public float getHorzposleftborder() {
        return horzPosLeftBorder;
    }

    public void setHorzposleftborder(float horzPosLeftBorder) {
        this.horzPosLeftBorder = horzPosLeftBorder;
    }
    public float getHorzposvalues() {
        return horzPosValues;
    }

    public void setHorzposvalues(float horzPosValues) {
        this.horzPosValues = horzPosValues;
    }
    public float getVertlinespace() {
        return vertLineSpace;
    }

    public void setVertlinespace(float vertLineSpace) {
        this.vertLineSpace = vertLineSpace;
    }
    public String getDatestamp() {
        return dateStamp;
    }

    public void setDatestamp(String dateStamp) {
        this.dateStamp = dateStamp;
    }
    public float getFonthightheader() {
        return fontHightHeader;
    }

    public void setFonthightheader(float fontHightHeader) {
        this.fontHightHeader = fontHightHeader;
    }
    public float getVertposheader() {
        return vertPosHeader;
    }

    public void setVertposheader(float vertPosHeader) {
        this.vertPosHeader = vertPosHeader;
    }

    public MachineLibrary_NodeSpecialConfiguration getMachinelibrary_nodespecialconfiguration() {
        return machinelibrary_nodespecialconfiguration;
    }

    public void setMachinelibrary_nodespecialconfiguration(MachineLibrary_NodeSpecialConfiguration machinelibrary_nodespecialconfiguration) {
        this.machinelibrary_nodespecialconfiguration = machinelibrary_nodespecialconfiguration;
    }

}