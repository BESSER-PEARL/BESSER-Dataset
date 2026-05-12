





import java.util.List;
import java.util.ArrayList;

public class Model_Chunk  {






    private List<Model_Tile> model_tiles;


    public Model_Chunk(
    ) {
        this.model_tiles = new ArrayList<>();
    }

    public Model_Chunk(
        ArrayList<Model_Tile> model_tiles    ) {
        this.model_tiles = model_tiles;
    }


    public List<Model_Tile> getModel_tiles() {
        return model_tiles;
    }

    public void addModel_tile(Model_tile model_tile) {
        this.model_tiles.add(model_tile);
    }

}