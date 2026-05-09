





import java.util.List;
import java.util.ArrayList;

public class mvc_Position  {

    private int long;
    private int above;
    private int align_left;
    private String name;
    private int wide;





    private mvc_View mvc_view;


    public mvc_Position(
        int long,        int above,        int align_left,        String name,        int wide    ) {
        this.long = long;
        this.above = above;
        this.align_left = align_left;
        this.name = name;
        this.wide = wide;
    }


    public int getLong() {
        return long;
    }

    public void setLong(int long) {
        this.long = long;
    }
    public int getAbove() {
        return above;
    }

    public void setAbove(int above) {
        this.above = above;
    }
    public int getAlign_left() {
        return align_left;
    }

    public void setAlign_left(int align_left) {
        this.align_left = align_left;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getWide() {
        return wide;
    }

    public void setWide(int wide) {
        this.wide = wide;
    }

    public mvc_View getMvc_view() {
        return mvc_view;
    }

    public void setMvc_view(mvc_View mvc_view) {
        this.mvc_view = mvc_view;
    }

}