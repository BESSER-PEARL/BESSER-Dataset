





import java.util.List;
import java.util.ArrayList;

public class ck2gfx_Animation  {

    private float defaultAnimationTime;
    private String file;
    private String name;





    private ck2gfx_EMFXActorType ck2gfx_emfxactortype;


    public ck2gfx_Animation(
        float defaultAnimationTime,        String file,        String name    ) {
        this.defaultAnimationTime = defaultAnimationTime;
        this.file = file;
        this.name = name;
    }


    public float getDefaultanimationtime() {
        return defaultAnimationTime;
    }

    public void setDefaultanimationtime(float defaultAnimationTime) {
        this.defaultAnimationTime = defaultAnimationTime;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ck2gfx_EMFXActorType getCk2gfx_emfxactortype() {
        return ck2gfx_emfxactortype;
    }

    public void setCk2gfx_emfxactortype(ck2gfx_EMFXActorType ck2gfx_emfxactortype) {
        this.ck2gfx_emfxactortype = ck2gfx_emfxactortype;
    }

}