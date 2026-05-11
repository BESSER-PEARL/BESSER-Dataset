





import java.util.List;
import java.util.ArrayList;

public class jpdl31_Factor  {

    private String isTreament;
    private String name;





    private List<jpdl31_Level> jpdl31_levels;


    public jpdl31_Factor(
        String isTreament,        String name    ) {
        this.isTreament = isTreament;
        this.name = name;
        this.jpdl31_levels = new ArrayList<>();
    }

    public jpdl31_Factor(
        String isTreament,        String name        ArrayList<jpdl31_Level> jpdl31_levels    ) {
        this.isTreament = isTreament;
        this.name = name;
        this.jpdl31_levels = jpdl31_levels;
    }

    public String getIstreament() {
        return isTreament;
    }

    public void setIstreament(String isTreament) {
        this.isTreament = isTreament;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<jpdl31_Level> getJpdl31_levels() {
        return jpdl31_levels;
    }

    public void addJpdl31_level(Jpdl31_level jpdl31_level) {
        this.jpdl31_levels.add(jpdl31_level);
    }

}