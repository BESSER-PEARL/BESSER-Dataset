





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Gate  {

    private float x;
    private String name;
    private String addlevel;
    private float y;
    private String symbol;
    private int swaplevel;





    private eaglemodel_Gates eaglemodel_gates;


    public eaglemodel_Gate(
        float x,        String name,        String addlevel,        float y,        String symbol,        int swaplevel    ) {
        this.x = x;
        this.name = name;
        this.addlevel = addlevel;
        this.y = y;
        this.symbol = symbol;
        this.swaplevel = swaplevel;
    }


    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddlevel() {
        return addlevel;
    }

    public void setAddlevel(String addlevel) {
        this.addlevel = addlevel;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }
    public int getSwaplevel() {
        return swaplevel;
    }

    public void setSwaplevel(int swaplevel) {
        this.swaplevel = swaplevel;
    }

    public eaglemodel_Gates getEaglemodel_gates() {
        return eaglemodel_gates;
    }

    public void setEaglemodel_gates(eaglemodel_Gates eaglemodel_gates) {
        this.eaglemodel_gates = eaglemodel_gates;
    }

}