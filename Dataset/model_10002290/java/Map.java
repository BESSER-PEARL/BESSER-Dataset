





import java.util.List;
import java.util.ArrayList;

public class Map  {






    private GameSession gamesession;




    private List<MapCell> mapcells;


    public Map(
    ) {
        this.mapcells = new ArrayList<>();
    }

    public Map(
        ArrayList<MapCell> mapcells    ) {
        this.mapcells = mapcells;
    }


    public GameSession getGamesession() {
        return gamesession;
    }

    public void setGamesession(GameSession gamesession) {
        this.gamesession = gamesession;
    }
    public List<MapCell> getMapcells() {
        return mapcells;
    }

    public void addMapcell(Mapcell mapcell) {
        this.mapcells.add(mapcell);
    }

}