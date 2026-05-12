





import java.util.List;
import java.util.ArrayList;

public class checkers_GameEngine  {

    private int king;
    private int normal;
    private int edge;
    private int inf;
    private int pos;



    public checkers_GameEngine(
        int king,        int normal,        int edge,        int inf,        int pos    ) {
        this.king = king;
        this.normal = normal;
        this.edge = edge;
        this.inf = inf;
        this.pos = pos;
    }


    public int getKing() {
        return king;
    }

    public void setKing(int king) {
        this.king = king;
    }
    public int getNormal() {
        return normal;
    }

    public void setNormal(int normal) {
        this.normal = normal;
    }
    public int getEdge() {
        return edge;
    }

    public void setEdge(int edge) {
        this.edge = edge;
    }
    public int getInf() {
        return inf;
    }

    public void setInf(int inf) {
        this.inf = inf;
    }
    public int getPos() {
        return pos;
    }

    public void setPos(int pos) {
        this.pos = pos;
    }


}