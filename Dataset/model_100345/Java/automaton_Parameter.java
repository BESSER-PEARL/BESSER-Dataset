





import java.util.List;
import java.util.ArrayList;

public class automaton_Parameter  {

    private int position;
    private String symbolicName;



    public automaton_Parameter(
        int position,        String symbolicName    ) {
        this.position = position;
        this.symbolicName = symbolicName;
    }


    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }
    public String getSymbolicname() {
        return symbolicName;
    }

    public void setSymbolicname(String symbolicName) {
        this.symbolicName = symbolicName;
    }


}