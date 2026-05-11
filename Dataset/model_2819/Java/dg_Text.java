





import java.util.List;
import java.util.ArrayList;

public class dg_Text extends GraphicalElement {

    private String anchor;
    private String data;





    private dg_Bounds dg_bounds;


    public dg_Text(
        String anchor,        String data    ) {
        super(
        );
        this.anchor = anchor;
        this.data = data;
    }


    public String getAnchor() {
        return anchor;
    }

    public void setAnchor(String anchor) {
        this.anchor = anchor;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public dg_Bounds getDg_bounds() {
        return dg_bounds;
    }

    public void setDg_bounds(dg_Bounds dg_bounds) {
        this.dg_bounds = dg_bounds;
    }

}