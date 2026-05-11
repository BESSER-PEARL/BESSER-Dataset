





import java.util.List;
import java.util.ArrayList;

public class Freemind_NodeType  {

    private String Style;
    private String EncryptedContent;
    private String Position;
    private String Modified;
    private String BackgroundColor;
    private String Text;
    private String Folded;
    private String Color;
    private String Link;
    private String Vgap;
    private String Created;
    private String Hgap;
    private String Vshift;
    private String group;
    private String Id;





    private List<Freemind_NodeType> freemind_nodetypes;




    private List<Freemind_ArrowlinkType> freemind_arrowlinktypes;




    private List<Freemind_CloudType> freemind_cloudtypes;




    private Freemind_MapType freemind_maptype;




    private Freemind_DocumentRoot freemind_documentroot;


    public Freemind_NodeType(
        String Style,        String EncryptedContent,        String Position,        String Modified,        String BackgroundColor,        String Text,        String Folded,        String Color,        String Link,        String Vgap,        String Created,        String Hgap,        String Vshift,        String group,        String Id    ) {
        this.Style = Style;
        this.EncryptedContent = EncryptedContent;
        this.Position = Position;
        this.Modified = Modified;
        this.BackgroundColor = BackgroundColor;
        this.Text = Text;
        this.Folded = Folded;
        this.Color = Color;
        this.Link = Link;
        this.Vgap = Vgap;
        this.Created = Created;
        this.Hgap = Hgap;
        this.Vshift = Vshift;
        this.group = group;
        this.Id = Id;
        this.freemind_nodetypes = new ArrayList<>();
        this.freemind_arrowlinktypes = new ArrayList<>();
        this.freemind_cloudtypes = new ArrayList<>();
    }

    public Freemind_NodeType(
        String Style,        String EncryptedContent,        String Position,        String Modified,        String BackgroundColor,        String Text,        String Folded,        String Color,        String Link,        String Vgap,        String Created,        String Hgap,        String Vshift,        String group,        String Id        ArrayList<Freemind_NodeType> freemind_nodetypes,        ArrayList<Freemind_ArrowlinkType> freemind_arrowlinktypes,        ArrayList<Freemind_CloudType> freemind_cloudtypes    ) {
        this.Style = Style;
        this.EncryptedContent = EncryptedContent;
        this.Position = Position;
        this.Modified = Modified;
        this.BackgroundColor = BackgroundColor;
        this.Text = Text;
        this.Folded = Folded;
        this.Color = Color;
        this.Link = Link;
        this.Vgap = Vgap;
        this.Created = Created;
        this.Hgap = Hgap;
        this.Vshift = Vshift;
        this.group = group;
        this.Id = Id;
        this.freemind_nodetypes = freemind_nodetypes;
        this.freemind_arrowlinktypes = freemind_arrowlinktypes;
        this.freemind_cloudtypes = freemind_cloudtypes;
    }

    public String getStyle() {
        return Style;
    }

    public void setStyle(String Style) {
        this.Style = Style;
    }
    public String getEncryptedcontent() {
        return EncryptedContent;
    }

    public void setEncryptedcontent(String EncryptedContent) {
        this.EncryptedContent = EncryptedContent;
    }
    public String getPosition() {
        return Position;
    }

    public void setPosition(String Position) {
        this.Position = Position;
    }
    public String getModified() {
        return Modified;
    }

    public void setModified(String Modified) {
        this.Modified = Modified;
    }
    public String getBackgroundcolor() {
        return BackgroundColor;
    }

    public void setBackgroundcolor(String BackgroundColor) {
        this.BackgroundColor = BackgroundColor;
    }
    public String getText() {
        return Text;
    }

    public void setText(String Text) {
        this.Text = Text;
    }
    public String getFolded() {
        return Folded;
    }

    public void setFolded(String Folded) {
        this.Folded = Folded;
    }
    public String getColor() {
        return Color;
    }

    public void setColor(String Color) {
        this.Color = Color;
    }
    public String getLink() {
        return Link;
    }

    public void setLink(String Link) {
        this.Link = Link;
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
    public String getHgap() {
        return Hgap;
    }

    public void setHgap(String Hgap) {
        this.Hgap = Hgap;
    }
    public String getVshift() {
        return Vshift;
    }

    public void setVshift(String Vshift) {
        this.Vshift = Vshift;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }

    public List<Freemind_NodeType> getFreemind_nodetypes() {
        return freemind_nodetypes;
    }

    public void addFreemind_nodetype(Freemind_nodetype freemind_nodetype) {
        this.freemind_nodetypes.add(freemind_nodetype);
    }
    public List<Freemind_ArrowlinkType> getFreemind_arrowlinktypes() {
        return freemind_arrowlinktypes;
    }

    public void addFreemind_arrowlinktype(Freemind_arrowlinktype freemind_arrowlinktype) {
        this.freemind_arrowlinktypes.add(freemind_arrowlinktype);
    }
    public List<Freemind_CloudType> getFreemind_cloudtypes() {
        return freemind_cloudtypes;
    }

    public void addFreemind_cloudtype(Freemind_cloudtype freemind_cloudtype) {
        this.freemind_cloudtypes.add(freemind_cloudtype);
    }
    public Freemind_MapType getFreemind_maptype() {
        return freemind_maptype;
    }

    public void setFreemind_maptype(Freemind_MapType freemind_maptype) {
        this.freemind_maptype = freemind_maptype;
    }
    public Freemind_DocumentRoot getFreemind_documentroot() {
        return freemind_documentroot;
    }

    public void setFreemind_documentroot(Freemind_DocumentRoot freemind_documentroot) {
        this.freemind_documentroot = freemind_documentroot;
    }

}