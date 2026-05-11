





import java.util.List;
import java.util.ArrayList;

public class carnot_INodeSymbol extends IGraphicalObject {

    private String yPos;
    private String height;
    private String width;
    private String shape;
    private String xPos;





    private List<carnot_GenericLinkConnectionType> carnot_genericlinkconnectiontypes;




    private carnot_GenericLinkConnectionType carnot_genericlinkconnectiontype;




    private List<carnot_GenericLinkConnectionType> carnot_genericlinkconnectiontypes;




    private carnot_GenericLinkConnectionType carnot_genericlinkconnectiontype;


    public carnot_INodeSymbol(
        String yPos,        String height,        String width,        String shape,        String xPos    ) {
        super(
        );
        this.yPos = yPos;
        this.height = height;
        this.width = width;
        this.shape = shape;
        this.xPos = xPos;
        this.carnot_genericlinkconnectiontypes = new ArrayList<>();
        this.carnot_genericlinkconnectiontypes = new ArrayList<>();
    }

    public carnot_INodeSymbol(
        String yPos,        String height,        String width,        String shape,        String xPos        ArrayList<carnot_GenericLinkConnectionType> carnot_genericlinkconnectiontypes,        ArrayList<carnot_GenericLinkConnectionType> carnot_genericlinkconnectiontypes    ) {
        this.yPos = yPos;
        this.height = height;
        this.width = width;
        this.shape = shape;
        this.xPos = xPos;
        this.carnot_genericlinkconnectiontypes = carnot_genericlinkconnectiontypes;
        this.carnot_genericlinkconnectiontypes = carnot_genericlinkconnectiontypes;
    }

    public String getYpos() {
        return yPos;
    }

    public void setYpos(String yPos) {
        this.yPos = yPos;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public String getXpos() {
        return xPos;
    }

    public void setXpos(String xPos) {
        this.xPos = xPos;
    }

    public List<carnot_GenericLinkConnectionType> getCarnot_genericlinkconnectiontypes() {
        return carnot_genericlinkconnectiontypes;
    }

    public void addCarnot_genericlinkconnectiontype(Carnot_genericlinkconnectiontype carnot_genericlinkconnectiontype) {
        this.carnot_genericlinkconnectiontypes.add(carnot_genericlinkconnectiontype);
    }
    public carnot_GenericLinkConnectionType getCarnot_genericlinkconnectiontype() {
        return carnot_genericlinkconnectiontype;
    }

    public void setCarnot_genericlinkconnectiontype(carnot_GenericLinkConnectionType carnot_genericlinkconnectiontype) {
        this.carnot_genericlinkconnectiontype = carnot_genericlinkconnectiontype;
    }
    public List<carnot_GenericLinkConnectionType> getCarnot_genericlinkconnectiontypes() {
        return carnot_genericlinkconnectiontypes;
    }

    public void addCarnot_genericlinkconnectiontype(Carnot_genericlinkconnectiontype carnot_genericlinkconnectiontype) {
        this.carnot_genericlinkconnectiontypes.add(carnot_genericlinkconnectiontype);
    }
    public carnot_GenericLinkConnectionType getCarnot_genericlinkconnectiontype() {
        return carnot_genericlinkconnectiontype;
    }

    public void setCarnot_genericlinkconnectiontype(carnot_GenericLinkConnectionType carnot_genericlinkconnectiontype) {
        this.carnot_genericlinkconnectiontype = carnot_genericlinkconnectiontype;
    }

}