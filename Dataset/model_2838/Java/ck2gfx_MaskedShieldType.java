





import java.util.List;
import java.util.ArrayList;

public class ck2gfx_MaskedShieldType  {

    private String name;
    private String clickSound;
    private String effectFile;
    private boolean allwaysTransparent;
    private String textureFile1;
    private String textureFile2;



    public ck2gfx_MaskedShieldType(
        String name,        String clickSound,        String effectFile,        boolean allwaysTransparent,        String textureFile1,        String textureFile2    ) {
        this.name = name;
        this.clickSound = clickSound;
        this.effectFile = effectFile;
        this.allwaysTransparent = allwaysTransparent;
        this.textureFile1 = textureFile1;
        this.textureFile2 = textureFile2;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getClicksound() {
        return clickSound;
    }

    public void setClicksound(String clickSound) {
        this.clickSound = clickSound;
    }
    public String getEffectfile() {
        return effectFile;
    }

    public void setEffectfile(String effectFile) {
        this.effectFile = effectFile;
    }
    public boolean getAllwaystransparent() {
        return allwaysTransparent;
    }

    public void setAllwaystransparent(boolean allwaysTransparent) {
        this.allwaysTransparent = allwaysTransparent;
    }
    public String getTexturefile1() {
        return textureFile1;
    }

    public void setTexturefile1(String textureFile1) {
        this.textureFile1 = textureFile1;
    }
    public String getTexturefile2() {
        return textureFile2;
    }

    public void setTexturefile2(String textureFile2) {
        this.textureFile2 = textureFile2;
    }


}