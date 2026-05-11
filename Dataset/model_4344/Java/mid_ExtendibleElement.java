





import java.util.List;
import java.util.ArrayList;

public class mid_ExtendibleElement  {

    private String level;
    private String metatypeUri;
    private boolean dynamic;
    private String uri;
    private String name;





    private mid_ExtendibleElement mid_extendibleelement;




    private mid_EStringToExtendibleElementMap mid_estringtoextendibleelementmap;


    public mid_ExtendibleElement(
        String level,        String metatypeUri,        boolean dynamic,        String uri,        String name    ) {
        this.level = level;
        this.metatypeUri = metatypeUri;
        this.dynamic = dynamic;
        this.uri = uri;
        this.name = name;
    }


    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }
    public String getMetatypeuri() {
        return metatypeUri;
    }

    public void setMetatypeuri(String metatypeUri) {
        this.metatypeUri = metatypeUri;
    }
    public boolean getDynamic() {
        return dynamic;
    }

    public void setDynamic(boolean dynamic) {
        this.dynamic = dynamic;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mid_ExtendibleElement getMid_extendibleelement() {
        return mid_extendibleelement;
    }

    public void setMid_extendibleelement(mid_ExtendibleElement mid_extendibleelement) {
        this.mid_extendibleelement = mid_extendibleelement;
    }
    public mid_EStringToExtendibleElementMap getMid_estringtoextendibleelementmap() {
        return mid_estringtoextendibleelementmap;
    }

    public void setMid_estringtoextendibleelementmap(mid_EStringToExtendibleElementMap mid_estringtoextendibleelementmap) {
        this.mid_estringtoextendibleelementmap = mid_estringtoextendibleelementmap;
    }

}