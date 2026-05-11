





import java.util.List;
import java.util.ArrayList;

public class game_Game  {

    private String name;
    private String version;



    public game_Game(
        String name,        String version    ) {
        this.name = name;
        this.version = version;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}