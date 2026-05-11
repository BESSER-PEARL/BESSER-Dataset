





import java.util.List;
import java.util.ArrayList;

public class ck2gfx_PortraitType  {

    private int eyeColorIndex;
    private int headgearThatHidesHair;
    private String layers;
    private int hairColorIndex;
    private String name;
    private String effectFile;





    private List<ck2gfx_Color> ck2gfx_colors;




    private List<ck2gfx_Color> ck2gfx_colors;


    public ck2gfx_PortraitType(
        int eyeColorIndex,        int headgearThatHidesHair,        String layers,        int hairColorIndex,        String name,        String effectFile    ) {
        this.eyeColorIndex = eyeColorIndex;
        this.headgearThatHidesHair = headgearThatHidesHair;
        this.layers = layers;
        this.hairColorIndex = hairColorIndex;
        this.name = name;
        this.effectFile = effectFile;
        this.ck2gfx_colors = new ArrayList<>();
        this.ck2gfx_colors = new ArrayList<>();
    }

    public ck2gfx_PortraitType(
        int eyeColorIndex,        int headgearThatHidesHair,        String layers,        int hairColorIndex,        String name,        String effectFile        ArrayList<ck2gfx_Color> ck2gfx_colors,        ArrayList<ck2gfx_Color> ck2gfx_colors    ) {
        this.eyeColorIndex = eyeColorIndex;
        this.headgearThatHidesHair = headgearThatHidesHair;
        this.layers = layers;
        this.hairColorIndex = hairColorIndex;
        this.name = name;
        this.effectFile = effectFile;
        this.ck2gfx_colors = ck2gfx_colors;
        this.ck2gfx_colors = ck2gfx_colors;
    }

    public int getEyecolorindex() {
        return eyeColorIndex;
    }

    public void setEyecolorindex(int eyeColorIndex) {
        this.eyeColorIndex = eyeColorIndex;
    }
    public int getHeadgearthathideshair() {
        return headgearThatHidesHair;
    }

    public void setHeadgearthathideshair(int headgearThatHidesHair) {
        this.headgearThatHidesHair = headgearThatHidesHair;
    }
    public String getLayers() {
        return layers;
    }

    public void setLayers(String layers) {
        this.layers = layers;
    }
    public int getHaircolorindex() {
        return hairColorIndex;
    }

    public void setHaircolorindex(int hairColorIndex) {
        this.hairColorIndex = hairColorIndex;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEffectfile() {
        return effectFile;
    }

    public void setEffectfile(String effectFile) {
        this.effectFile = effectFile;
    }

    public List<ck2gfx_Color> getCk2gfx_colors() {
        return ck2gfx_colors;
    }

    public void addCk2gfx_color(Ck2gfx_color ck2gfx_color) {
        this.ck2gfx_colors.add(ck2gfx_color);
    }
    public List<ck2gfx_Color> getCk2gfx_colors() {
        return ck2gfx_colors;
    }

    public void addCk2gfx_color(Ck2gfx_color ck2gfx_color) {
        this.ck2gfx_colors.add(ck2gfx_color);
    }

}