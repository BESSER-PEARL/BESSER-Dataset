





import java.util.List;
import java.util.ArrayList;

public class stuff_Property  {

    private String name;
    private boolean intrinsic;





    private stuff_Thing stuff_thing;


    public stuff_Property(
        String name,        boolean intrinsic    ) {
        this.name = name;
        this.intrinsic = intrinsic;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIntrinsic() {
        return intrinsic;
    }

    public void setIntrinsic(boolean intrinsic) {
        this.intrinsic = intrinsic;
    }

    public stuff_Thing getStuff_thing() {
        return stuff_thing;
    }

    public void setStuff_thing(stuff_Thing stuff_thing) {
        this.stuff_thing = stuff_thing;
    }

}