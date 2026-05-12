





import java.util.List;
import java.util.ArrayList;

public class solid1  {

    private int pieces;
    private String weight__kg_;
    private String state;
    private String name;



    public solid1(
        int pieces,        String weight__kg_,        String state,        String name    ) {
        this.pieces = pieces;
        this.weight__kg_ = weight__kg_;
        this.state = state;
        this.name = name;
    }


    public int getPieces() {
        return pieces;
    }

    public void setPieces(int pieces) {
        this.pieces = pieces;
    }
    public String getWeight__kg_() {
        return weight__kg_;
    }

    public void setWeight__kg_(String weight__kg_) {
        this.weight__kg_ = weight__kg_;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}