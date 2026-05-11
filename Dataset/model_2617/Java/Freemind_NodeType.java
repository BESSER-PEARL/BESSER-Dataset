





import java.util.List;
import java.util.ArrayList;

public class Freemind_NodeType  {

    private String Position;
    private String Link;
    private String Modified;
    private String Vshift;
    private String Id;
    private String EncryptedContent;
    private String Vgap;
    private String Created;
    private String group;
    private String Style;
    private String Color;
    private String Hgap;
    private String Folded;
    private String Text;
    private String BackgroundColor;





    private List<Freemind_ArrowlinkType> freemind_arrowlinktypes;




    private List<Freemind_EdgeType> freemind_edgetypes;




    private Freemind_MapType freemind_maptype;




    private List<Freemind_CloudType> freemind_cloudtypes;




    private Freemind_DocumentRoot freemind_documentroot;




    private List<Freemind_NodeType> freemind_nodetypes;


    public Freemind_NodeType(
        String Position,        String Link,        String Modified,        String Vshift,        String Id,        String EncryptedContent,        String Vgap,        String Created,        String group,        String Style,        String Color,        String Hgap,        String Folded,        String Text,        String BackgroundColor    ) {
        this.Position = Position;
        this.Link = Link;
        this.Modified = Modified;
        this.Vshift = Vshift;
        this.Id = Id;
        this.EncryptedContent = EncryptedContent;
        this.Vgap = Vgap;
        this.Created = Created;
        this.group = group;
        this.Style = Style;
        this.Color = Color;
        this.Hgap = Hgap;
        this.Folded = Folded;
        this.Text = Text;
        this.BackgroundColor = BackgroundColor;
        this.freemind_arrowlinktypes = new ArrayList<>();
        this.freemind_edgetypes = new ArrayList<>();
        this.freemind_cloudtypes = new ArrayList<>();
        this.freemind_nodetypes = new ArrayList<>();
    }

    public Freemind_NodeType(
        String Position,        String Link,        String Modified,        String Vshift,        String Id,        String EncryptedContent,        String Vgap,        String Created,        String group,        String Style,        String Color,        String Hgap,        String Folded,        String Text,        String BackgroundColor        ArrayList<Freemind_ArrowlinkType> freemind_arrowlinktypes,        ArrayList<Freemind_EdgeType> freemind_edgetypes,        ArrayList<Freemind_CloudType> freemind_cloudtypes,        ArrayList<Freemind_NodeType> freemind_nodetypes    ) {
        this.Position = Position;
        this.Link = Link;
        this.Modified = Modified;
        this.Vshift = Vshift;
        this.Id = Id;
        this.EncryptedContent = EncryptedContent;
        this.Vgap = Vgap;
        this.Created = Created;
        this.group = group;
        this.Style = Style;
        this.Color = Color;
        this.Hgap = Hgap;
        this.Folded = Folded;
        this.Text = Text;
        this.BackgroundColor = BackgroundColor;
        this.freemind_arrowlinktypes = freemind_arrowlinktypes;
        this.freemind_edgetypes = freemind_edgetypes;
        this.freemind_cloudtypes = freemind_cloudtypes;
        this.freemind_nodetypes = freemind_nodetypes;
    }

    public String getPosition() {
        return Position;
    }

    public void setPosition(String Position) {
        this.Position = Position;
    }
    public String getLink() {
        return Link;
    }

    public void setLink(String Link) {
        this.Link = Link;
    }
    public String getModified() {
        return Modified;
    }

    public void setModified(String Modified) {
        this.Modified = Modified;
    }
    public String getVshift() {
        return Vshift;
    }

    public void setVshift(String Vshift) {
        this.Vshift = Vshift;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public String getEncryptedcontent() {
        return EncryptedContent;
    }

    public void setEncryptedcontent(String EncryptedContent) {
        this.EncryptedContent = EncryptedContent;
    }
    public String getVgap() {
        return Vgap;
    }

    public void setVgap(String Vgap) {
        this.Vgap = Vgap;
    }
    public String getCreated() {
        return Created;
    }

    public void setCreated(String Created) {
        this.Created = Created;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getStyle() {
        return Style;
    }

    public void setStyle(String Style) {
        this.Style = Style;
    }
    public String getColor() {
        return Color;
    }

    public void setColor(String Color) {
        this.Color = Color;
    }
    public String getHgap() {
        return Hgap;
    }

    public void setHgap(String Hgap) {
        this.Hgap = Hgap;
    }
    public String getFolded() {
        return Folded;
    }

    public void setFolded(String Folded) {
        this.Folded = Folded;
    }
    public String getText() {
        return Text;
    }

    public void setText(String Text) {
        this.Text = Text;
    }
    public String getBackgroundcolor() {
        return BackgroundColor;
    }

    public void setBackgroundcolor(String BackgroundColor) {
        this.BackgroundColor = BackgroundColor;
    }

    public List<Freemind_ArrowlinkType> getFreemind_arrowlinktypes() {
        return freemind_arrowlinktypes;
    }

    public void addFreemind_arrowlinktype(Freemind_arrowlinktype freemind_arrowlinktype) {
        this.freemind_arrowlinktypes.add(freemind_arrowlinktype);
    }
    public List<Freemind_EdgeType> getFreemind_edgetypes() {
        return freemind_edgetypes;
    }

    public void addFreemind_edgetype(Freemind_edgetype freemind_edgetype) {
        this.freemind_edgetypes.add(freemind_edgetype);
    }
    public Freemind_MapType getFreemind_maptype() {
        return freemind_maptype;
    }

    public void setFreemind_maptype(Freemind_MapType freemind_maptype) {
        this.freemind_maptype = freemind_maptype;
    }
    public List<Freemind_CloudType> getFreemind_cloudtypes() {
        return freemind_cloudtypes;
    }

    public void addFreemind_cloudtype(Freemind_cloudtype freemind_cloudtype) {
        this.freemind_cloudtypes.add(freemind_cloudtype);
    }
    public Freemind_DocumentRoot getFreemind_documentroot() {
        return freemind_documentroot;
    }

    public void setFreemind_documentroot(Freemind_DocumentRoot freemind_documentroot) {
        this.freemind_documentroot = freemind_documentroot;
    }
    public List<Freemind_NodeType> getFreemind_nodetypes() {
        return freemind_nodetypes;
    }

    public void addFreemind_nodetype(Freemind_nodetype freemind_nodetype) {
        this.freemind_nodetypes.add(freemind_nodetype);
    }

}