





import java.util.List;
import java.util.ArrayList;

public class syswbeff1065ok_Thoughts  {

    private String id;





    private List<syswbeff1065ok_Thing> syswbeff1065ok_things;


    public syswbeff1065ok_Thoughts(
        String id    ) {
        this.id = id;
        this.syswbeff1065ok_things = new ArrayList<>();
    }

    public syswbeff1065ok_Thoughts(
        String id        ArrayList<syswbeff1065ok_Thing> syswbeff1065ok_things    ) {
        this.id = id;
        this.syswbeff1065ok_things = syswbeff1065ok_things;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<syswbeff1065ok_Thing> getSyswbeff1065ok_things() {
        return syswbeff1065ok_things;
    }

    public void addSyswbeff1065ok_thing(Syswbeff1065ok_thing syswbeff1065ok_thing) {
        this.syswbeff1065ok_things.add(syswbeff1065ok_thing);
    }

}