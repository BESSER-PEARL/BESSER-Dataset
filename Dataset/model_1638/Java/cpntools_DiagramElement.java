





import java.util.List;
import java.util.ArrayList;

public class cpntools_DiagramElement  {

    private String fillColour;
    private String lineType;
    private int posy;
    private int posx;
    private String lineColour;
    private String fillPattern;
    private boolean fillFilled;
    private int lineThick;





    private cpntools_Group cpntools_group;




    private cpntools_Group cpntools_group;


    public cpntools_DiagramElement(
        String fillColour,        String lineType,        int posy,        int posx,        String lineColour,        String fillPattern,        boolean fillFilled,        int lineThick    ) {
        this.fillColour = fillColour;
        this.lineType = lineType;
        this.posy = posy;
        this.posx = posx;
        this.lineColour = lineColour;
        this.fillPattern = fillPattern;
        this.fillFilled = fillFilled;
        this.lineThick = lineThick;
    }


    public String getFillcolour() {
        return fillColour;
    }

    public void setFillcolour(String fillColour) {
        this.fillColour = fillColour;
    }
    public String getLinetype() {
        return lineType;
    }

    public void setLinetype(String lineType) {
        this.lineType = lineType;
    }
    public int getPosy() {
        return posy;
    }

    public void setPosy(int posy) {
        this.posy = posy;
    }
    public int getPosx() {
        return posx;
    }

    public void setPosx(int posx) {
        this.posx = posx;
    }
    public String getLinecolour() {
        return lineColour;
    }

    public void setLinecolour(String lineColour) {
        this.lineColour = lineColour;
    }
    public String getFillpattern() {
        return fillPattern;
    }

    public void setFillpattern(String fillPattern) {
        this.fillPattern = fillPattern;
    }
    public boolean getFillfilled() {
        return fillFilled;
    }

    public void setFillfilled(boolean fillFilled) {
        this.fillFilled = fillFilled;
    }
    public int getLinethick() {
        return lineThick;
    }

    public void setLinethick(int lineThick) {
        this.lineThick = lineThick;
    }

    public cpntools_Group getCpntools_group() {
        return cpntools_group;
    }

    public void setCpntools_group(cpntools_Group cpntools_group) {
        this.cpntools_group = cpntools_group;
    }
    public cpntools_Group getCpntools_group() {
        return cpntools_group;
    }

    public void setCpntools_group(cpntools_Group cpntools_group) {
        this.cpntools_group = cpntools_group;
    }

}