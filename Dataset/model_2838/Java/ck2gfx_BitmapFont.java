





import java.util.List;
import java.util.ArrayList;

public class ck2gfx_BitmapFont  {

    private boolean effect;
    private String fontName;
    private String name;
    private int color;





    private ck2gfx_BitmapFonts ck2gfx_bitmapfonts;


    public ck2gfx_BitmapFont(
        boolean effect,        String fontName,        String name,        int color    ) {
        this.effect = effect;
        this.fontName = fontName;
        this.name = name;
        this.color = color;
    }


    public boolean getEffect() {
        return effect;
    }

    public void setEffect(boolean effect) {
        this.effect = effect;
    }
    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getColor() {
        return color;
    }

    public void setColor(int color) {
        this.color = color;
    }

    public ck2gfx_BitmapFonts getCk2gfx_bitmapfonts() {
        return ck2gfx_bitmapfonts;
    }

    public void setCk2gfx_bitmapfonts(ck2gfx_BitmapFonts ck2gfx_bitmapfonts) {
        this.ck2gfx_bitmapfonts = ck2gfx_bitmapfonts;
    }

}