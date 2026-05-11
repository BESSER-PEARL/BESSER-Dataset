





import java.util.List;
import java.util.ArrayList;

public class ck2gfx_ArrowType  {

    private String name;
    private float height;
    private float size;
    private float endAt;
    private int type;
    private String bodyTexture;
    private String effect;
    private float heading;
    private String textureFile;





    private ck2gfx_ColorRatio ck2gfx_colorratio;




    private ck2gfx_ColorRatio ck2gfx_colorratio;


    public ck2gfx_ArrowType(
        String name,        float height,        float size,        float endAt,        int type,        String bodyTexture,        String effect,        float heading,        String textureFile    ) {
        this.name = name;
        this.height = height;
        this.size = size;
        this.endAt = endAt;
        this.type = type;
        this.bodyTexture = bodyTexture;
        this.effect = effect;
        this.heading = heading;
        this.textureFile = textureFile;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public float getSize() {
        return size;
    }

    public void setSize(float size) {
        this.size = size;
    }
    public float getEndat() {
        return endAt;
    }

    public void setEndat(float endAt) {
        this.endAt = endAt;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public String getBodytexture() {
        return bodyTexture;
    }

    public void setBodytexture(String bodyTexture) {
        this.bodyTexture = bodyTexture;
    }
    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }
    public float getHeading() {
        return heading;
    }

    public void setHeading(float heading) {
        this.heading = heading;
    }
    public String getTexturefile() {
        return textureFile;
    }

    public void setTexturefile(String textureFile) {
        this.textureFile = textureFile;
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