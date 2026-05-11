





import java.util.List;
import java.util.ArrayList;

public class delphi_MineID extends ident {

    private String second;
    private String first;



    public delphi_MineID(
        String second,        String first    ) {
        super(
        );
        this.second = second;
        this.first = first;
    }


    public String getSecond() {
        return second;
    }

    public void setSecond(String second) {
        this.second = second;
    }
    public String getFirst() {
        return first;
    }

    public void setFirst(String first) {
        this.first = first;
    }


}