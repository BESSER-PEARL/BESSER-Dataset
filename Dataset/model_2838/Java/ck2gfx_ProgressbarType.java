





import java.util.List;
import java.util.ArrayList;

public class ck2gfx_ProgressbarType  {

    private boolean noRefCount;
    private String loadType;
    private String textureFile1;
    private String effectFile;
    private String name;
    private String textureFile2;
    private boolean horizontal;
    private boolean allwaysTransparent;
    private float maxValue;





    private ck2gfx_Coordinates ck2gfx_coordinates;




    private ck2gfx_ColorRatio ck2gfx_colorratio;




    private ck2gfx_ColorRatio ck2gfx_colorratio;


    public ck2gfx_ProgressbarType(
        boolean noRefCount,        String loadType,        String textureFile1,        String effectFile,        String name,        String textureFile2,        boolean horizontal,        boolean allwaysTransparent,        float maxValue    ) {
        this.noRefCount = noRefCount;
        this.loadType = loadType;
        this.textureFile1 = textureFile1;
        this.effectFile = effectFile;
        this.name = name;
        this.textureFile2 = textureFile2;
        this.horizontal = horizontal;
        this.allwaysTransparent = allwaysTransparent;
        this.maxValue = maxValue;
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
    public String getTexturefile1() {
        return textureFile1;
    }

    public void setTexturefile1(String textureFile1) {
        this.textureFile1 = textureFile1;
    }
    public String getEffectfile() {
        return effectFile;
    }

    public void setEffectfile(String effectFile) {
        this.effectFile = effectFile;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTexturefile2() {
        return textureFile2;
    }

    public void setTexturefile2(String textureFile2) {
        this.textureFile2 = textureFile2;
    }
    public boolean getHorizontal() {
        return horizontal;
    }

    public void setHorizontal(boolean horizontal) {
        this.horizontal = horizontal;
    }
    public boolean getAllwaystransparent() {
        return allwaysTransparent;
    }

    public void setAllwaystransparent(boolean allwaysTransparent) {
        this.allwaysTransparent = allwaysTransparent;
    }
    public float getMaxvalue() {
        return maxValue;
    }

    public void setMaxvalue(float maxValue) {
        this.maxValue = maxValue;
    }

    public ck2gfx_Coordinates getCk2gfx_coordinates() {
        return ck2gfx_coordinates;
    }

    public void setCk2gfx_coordinates(ck2gfx_Coordinates ck2gfx_coordinates) {
        this.ck2gfx_coordinates = ck2gfx_coordinates;
    }
    public ck2gfx_ColorRatio getCk2gfx_colorratio() {
        return ck2gfx_colorratio;
    }

    public void setCk2gfx_colorratio(ck2gfx_ColorRatio ck2gfx_colorratio) {
        this.ck2gfx_colorratio = ck2gfx_colorratio;
    }
    public ck2gfx_ColorRatio getCk2gfx_colorratio() {
        return ck2gfx_colorratio;
    }

    public void setCk2gfx_colorratio(ck2gfx_ColorRatio ck2gfx_colorratio) {
        this.ck2gfx_colorratio = ck2gfx_colorratio;
    }

}