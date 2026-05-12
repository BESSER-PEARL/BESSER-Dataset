





import java.util.List;
import java.util.ArrayList;

public class pushbuttonbuild_DocumentRoot  {

    private String mixed;





    private List<pushbuttonbuild_BuildType> pushbuttonbuild_buildtypes;




    private List<pushbuttonbuild_ExtraZIPType> pushbuttonbuild_extraziptypes;


    public pushbuttonbuild_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.pushbuttonbuild_buildtypes = new ArrayList<>();
        this.pushbuttonbuild_extraziptypes = new ArrayList<>();
    }

    public pushbuttonbuild_DocumentRoot(
        String mixed        ArrayList<pushbuttonbuild_BuildType> pushbuttonbuild_buildtypes,        ArrayList<pushbuttonbuild_ExtraZIPType> pushbuttonbuild_extraziptypes    ) {
        this.mixed = mixed;
        this.pushbuttonbuild_buildtypes = pushbuttonbuild_buildtypes;
        this.pushbuttonbuild_extraziptypes = pushbuttonbuild_extraziptypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<pushbuttonbuild_BuildType> getPushbuttonbuild_buildtypes() {
        return pushbuttonbuild_buildtypes;
    }

    public void addPushbuttonbuild_buildtype(Pushbuttonbuild_buildtype pushbuttonbuild_buildtype) {
        this.pushbuttonbuild_buildtypes.add(pushbuttonbuild_buildtype);
    }
    public List<pushbuttonbuild_ExtraZIPType> getPushbuttonbuild_extraziptypes() {
        return pushbuttonbuild_extraziptypes;
    }

    public void addPushbuttonbuild_extraziptype(Pushbuttonbuild_extraziptype pushbuttonbuild_extraziptype) {
        this.pushbuttonbuild_extraziptypes.add(pushbuttonbuild_extraziptype);
    }

}