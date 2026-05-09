





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Frame  {

    private int rows;
    private int layer;
    private boolean borderleft;
    private float x2;
    private boolean bordertop;
    private float y2;
    private boolean borderbottom;
    private float x1;
    private int columns;
    private float y1;
    private boolean borderright;





    private eaglemodel_Package eaglemodel_package;




    private eaglemodel_Plain eaglemodel_plain;


    public eaglemodel_Frame(
        int rows,        int layer,        boolean borderleft,        float x2,        boolean bordertop,        float y2,        boolean borderbottom,        float x1,        int columns,        float y1,        boolean borderright    ) {
        this.rows = rows;
        this.layer = layer;
        this.borderleft = borderleft;
        this.x2 = x2;
        this.bordertop = bordertop;
        this.y2 = y2;
        this.borderbottom = borderbottom;
        this.x1 = x1;
        this.columns = columns;
        this.y1 = y1;
        this.borderright = borderright;
    }


    public int getRows() {
        return rows;
    }

    public void setRows(int rows) {
        this.rows = rows;
    }
    public int getLayer() {
        return layer;
    }

    public void setLayer(int layer) {
        this.layer = layer;
    }
    public boolean getBorderleft() {
        return borderleft;
    }

    public void setBorderleft(boolean borderleft) {
        this.borderleft = borderleft;
    }
    public float getX2() {
        return x2;
    }

    public void setX2(float x2) {
        this.x2 = x2;
    }
    public boolean getBordertop() {
        return bordertop;
    }

    public void setBordertop(boolean bordertop) {
        this.bordertop = bordertop;
    }
    public float getY2() {
        return y2;
    }

    public void setY2(float y2) {
        this.y2 = y2;
    }
    public boolean getBorderbottom() {
        return borderbottom;
    }

    public void setBorderbottom(boolean borderbottom) {
        this.borderbottom = borderbottom;
    }
    public float getX1() {
        return x1;
    }

    public void setX1(float x1) {
        this.x1 = x1;
    }
    public int getColumns() {
        return columns;
    }

    public void setColumns(int columns) {
        this.columns = columns;
    }
    public float getY1() {
        return y1;
    }

    public void setY1(float y1) {
        this.y1 = y1;
    }
    public boolean getBorderright() {
        return borderright;
    }

    public void setBorderright(boolean borderright) {
        this.borderright = borderright;
    }

    public eaglemodel_Package getEaglemodel_package() {
        return eaglemodel_package;
    }

    public void setEaglemodel_package(eaglemodel_Package eaglemodel_package) {
        this.eaglemodel_package = eaglemodel_package;
    }
    public eaglemodel_Plain getEaglemodel_plain() {
        return eaglemodel_plain;
    }

    public void setEaglemodel_plain(eaglemodel_Plain eaglemodel_plain) {
        this.eaglemodel_plain = eaglemodel_plain;
    }

}