





import java.util.List;
import java.util.ArrayList;

public class ck2gfx_SpriteTypes  {






    private List<ck2gfx_EObject> ck2gfx_eobjects;


    public ck2gfx_SpriteTypes(
    ) {
        this.ck2gfx_eobjects = new ArrayList<>();
    }

    public ck2gfx_SpriteTypes(
        ArrayList<ck2gfx_EObject> ck2gfx_eobjects    ) {
        this.ck2gfx_eobjects = ck2gfx_eobjects;
    }


    public List<ck2gfx_EObject> getCk2gfx_eobjects() {
        return ck2gfx_eobjects;
    }

    public void addCk2gfx_eobject(Ck2gfx_eobject ck2gfx_eobject) {
        this.ck2gfx_eobjects.add(ck2gfx_eobject);
    }

}