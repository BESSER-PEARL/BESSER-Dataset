





import java.util.List;
import java.util.ArrayList;

public class helloworld123_World  {






    private List<helloworld123_Thing> helloworld123_things;


    public helloworld123_World(
    ) {
        this.helloworld123_things = new ArrayList<>();
    }

    public helloworld123_World(
        ArrayList<helloworld123_Thing> helloworld123_things    ) {
        this.helloworld123_things = helloworld123_things;
    }


    public List<helloworld123_Thing> getHelloworld123_things() {
        return helloworld123_things;
    }

    public void addHelloworld123_thing(Helloworld123_thing helloworld123_thing) {
        this.helloworld123_things.add(helloworld123_thing);
    }

}