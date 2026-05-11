





import java.util.List;
import java.util.ArrayList;

public class dsl_Mover  {

    private String pathfindingMode;
    private String standingMode;
    private String name;
    private String heightmap;



    public dsl_Mover(
        String pathfindingMode,        String standingMode,        String name,        String heightmap    ) {
        this.pathfindingMode = pathfindingMode;
        this.standingMode = standingMode;
        this.name = name;
        this.heightmap = heightmap;
    }


    public String getPathfindingmode() {
        return pathfindingMode;
    }

    public void setPathfindingmode(String pathfindingMode) {
        this.pathfindingMode = pathfindingMode;
    }
    public String getStandingmode() {
        return standingMode;
    }

    public void setStandingmode(String standingMode) {
        this.standingMode = standingMode;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getHeightmap() {
        return heightmap;
    }

    public void setHeightmap(String heightmap) {
        this.heightmap = heightmap;
    }


}