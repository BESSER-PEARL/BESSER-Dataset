





import java.util.List;
import java.util.ArrayList;

public class ck2gfx_CorneredTileSpriteType  {

    private boolean tilingCenter;
    private boolean allwaysTransparent;
    private boolean noRefCount;
    private String loadType;
    private String name;
    private String texturefile;





    private ck2gfx_Coordinates ck2gfx_coordinates;




    private ck2gfx_Coordinates ck2gfx_coordinates;


    public ck2gfx_CorneredTileSpriteType(
        boolean tilingCenter,        boolean allwaysTransparent,        boolean noRefCount,        String loadType,        String name,        String texturefile    ) {
        this.tilingCenter = tilingCenter;
        this.allwaysTransparent = allwaysTransparent;
        this.noRefCount = noRefCount;
        this.loadType = loadType;
        this.name = name;
        this.texturefile = texturefile;
    }


    public boolean getTilingcenter() {
        return tilingCenter;
    }

    public void setTilingcenter(boolean tilingCenter) {
        this.tilingCenter = tilingCenter;
    }
    public boolean getAllwaystransparent() {
        return allwaysTransparent;
    }

    public void setAllwaystransparent(boolean allwaysTransparent) {
        this.allwaysTransparent = allwaysTransparent;
    }
    public boolean getNorefcount() {
        return noRefCount;
    }

    public void setNorefcount(boolean noRefCount) {
        this.noRefCount = noRefCount;
    }
    public String getLoadtype() {
        return loadType;
    }

    public void setLoadtype(String loadType) {
        this.loadType = loadType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTexturefile() {
        return texturefile;
    }

    public void setTexturefile(String texturefile) {
        this.texturefile = texturefile;
    }

    public ck2gfx_Coordinates getCk2gfx_coordinates() {
        return ck2gfx_coordinates;
    }

    public void setCk2gfx_coordinates(ck2gfx_Coordinates ck2gfx_coordinates) {
        this.ck2gfx_coordinates = ck2gfx_coordinates;
    }
    public ck2gfx_Coordinates getCk2gfx_coordinates() {
        return ck2gfx_coordinates;
    }

    public void setCk2gfx_coordinates(ck2gfx_Coordinates ck2gfx_coordinates) {
        this.ck2gfx_coordinates = ck2gfx_coordinates;
    }

}