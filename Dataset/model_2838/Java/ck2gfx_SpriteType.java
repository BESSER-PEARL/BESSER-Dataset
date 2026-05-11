





import java.util.List;
import java.util.ArrayList;

public class ck2gfx_SpriteType  {

    private String textureFile;
    private boolean transparenceCheck;
    private String loadType;
    private String clickSound;
    private boolean noRefCount;
    private String effectFile;
    private String name;
    private boolean canBeLowres;
    private boolean allwaysTransparent;
    private int noOfFrames;



    public ck2gfx_SpriteType(
        String textureFile,        boolean transparenceCheck,        String loadType,        String clickSound,        boolean noRefCount,        String effectFile,        String name,        boolean canBeLowres,        boolean allwaysTransparent,        int noOfFrames    ) {
        this.textureFile = textureFile;
        this.transparenceCheck = transparenceCheck;
        this.loadType = loadType;
        this.clickSound = clickSound;
        this.noRefCount = noRefCount;
        this.effectFile = effectFile;
        this.name = name;
        this.canBeLowres = canBeLowres;
        this.allwaysTransparent = allwaysTransparent;
        this.noOfFrames = noOfFrames;
    }


    public String getTexturefile() {
        return textureFile;
    }

    public void setTexturefile(String textureFile) {
        this.textureFile = textureFile;
    }
    public boolean getTransparencecheck() {
        return transparenceCheck;
    }

    public void setTransparencecheck(boolean transparenceCheck) {
        this.transparenceCheck = transparenceCheck;
    }
    public String getLoadtype() {
        return loadType;
    }

    public void setLoadtype(String loadType) {
        this.loadType = loadType;
    }
    public String getClicksound() {
        return clickSound;
    }

    public void setClicksound(String clickSound) {
        this.clickSound = clickSound;
    }
    public boolean getNorefcount() {
        return noRefCount;
    }

    public void setNorefcount(boolean noRefCount) {
        this.noRefCount = noRefCount;
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
    public boolean getCanbelowres() {
        return canBeLowres;
    }

    public void setCanbelowres(boolean canBeLowres) {
        this.canBeLowres = canBeLowres;
    }
    public boolean getAllwaystransparent() {
        return allwaysTransparent;
    }

    public void setAllwaystransparent(boolean allwaysTransparent) {
        this.allwaysTransparent = allwaysTransparent;
    }
    public int getNoofframes() {
        return noOfFrames;
    }

    public void setNoofframes(int noOfFrames) {
        this.noOfFrames = noOfFrames;
    }


}