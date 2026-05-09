





import java.util.List;
import java.util.ArrayList;

public class hello123_Property  {

    private String value;
    private String name;





    private hello123_Thing hello123_thing;


    public hello123_Property(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public hello123_Thing getHello123_thing() {
        return hello123_thing;
    }

    public void setHello123_thing(hello123_Thing hello123_thing) {
        this.hello123_thing = hello123_thing;
    }

}